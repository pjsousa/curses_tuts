import pandas as pd
import numpy as np
import hashlib
from io import StringIO

MAX_COLUMN_SIZE = 50
PADDING_SIZE = 2

class PandasRenderer():

	def __init__(self, df, x=0, y=0, width=np.inf, height=np.inf, preinit=True):
		self.df = df
		self.data_slice = None
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.col_str = dict()
		self.col_maxsizes = dict()
		self.col_minsizes = dict()
		self.col_offsets = []
		self.last_render = ""

		if preinit:
			self.slice_data(y,height)
			self.calc_column_sizes()
			self.calc_columns_offsets()
			self.render(newwidth=width, newheight=height)

	def slice_data(self, y, height, inplace=True):
		height = min(height, self.df.shape[0])
		data_slice = self.df.iloc[y:y+height]
		if inplace:
			self.y = y
			self.height = height
			self.data_slice = data_slice

		return data_slice

	def calc_column_sizes(self, data_slice=None, inplace=True):
		if data_slice is not None and inplace == True:
			raise ValueError("inplace cannot be True when data_slice != None")

		col_str = dict()
		col_minsizes = dict()
		col_maxsizes = dict()

		data_slice = self.data_slice if data_slice is None else data_slice

		for c in data_slice.columns:
			col_str[c] = data_slice[c].apply(str)
			col_minsizes[c] = col_str[c].str.len().min()
			col_maxsizes[c] = col_str[c].str.len().max()

			if inplace:
				self.col_str[c] = col_str[c]
				self.col_minsizes[c] = col_minsizes[c]
				self.col_maxsizes[c] = col_maxsizes[c]

		return col_str, col_minsizes, col_maxsizes

	def calc_columns_offsets(self, col_maxsizes=None, inplace=True):
		if col_maxsizes is not None and inplace == True:
			raise ValueError("inplace cannot be True when col_maxsizes != None")
		
		offset = 0
		size = 0

		col_maxsizes = self.col_maxsizes if col_maxsizes is None else col_maxsizes

		col_offsets = []

		for c in col_maxsizes:
			size = col_maxsizes[c]
			col_offsets.append([c, offset, size])
			offset += size + PADDING_SIZE

		if inplace:
			self.col_offsets = col_offsets

		return col_offsets

	def render(self, deltax=0, deltay=0, newwidth=None, newheight=None):
		changed_v = False

		if deltay != 0 or newheight is not None:
			newheight = newheight if newheight is not None else self.height
			self.slice_data(self.y+deltay,newheight)
			self.calc_column_sizes()
			self.calc_columns_offsets()
			changed_v = True
		if deltax != 0 or newwidth is not None:
			self.x = self.x + deltax
			self.width = self.width if newwidth is None else newwidth

		max_offset = sum(self.col_offsets[-1][1:])

		col_0 = max(self.x,0)
		col_1 = min(self.x+self.width, max_offset)

		if changed_v:
			render_df = pd.DataFrame()

			for c in self.data_slice.columns:
				s = self.col_str[c].apply(lambda x : \
									format(x, ">"+str(min(MAX_COLUMN_SIZE, self.col_maxsizes[c]))) \
									if len(x) <= MAX_COLUMN_SIZE \
									else x[:MAX_COLUMN_SIZE-5] + "[...]")
				render_df[c] = s

			render_str = render_df.to_string(index=False, header=False)

			self.last_render = render_str
		else:
			render_str = self.last_render


		render_str = [ x[col_0:col_1] for x in render_str.split("\n")]
		render_str = "\n".join(render_str)

		return render_str

	def get_offsets():
		return [ x[:] for x in self.col_offsets]


