from io import StringIO
import numpy as np
import pandas as pd
import hashlib
import pdrenderer
from pdrenderer import PandasRenderer
import json

def data_tiny():
	data={
		"seq_num": [0, 1, 2, 3, 4],
		"float": [0.000000, 0.344828, 0.689655, 1.034483, 1.379310],
		"float_neg": [-10.000000, -9.655172, -9.310345, -8.965517, -8.620690],
		"random": [0.469527, 0.104732, 0.975000, 0.349125, 0.124884],
		"dates": ["2018-01-01","2018-01-02","2018-01-03","2018-01-04","2018-01-05"],
		"datetimes": ["2018-01-01 00:00:00","2018-01-01 01:00:00","2018-01-01 02:00:00","2018-01-01 03:00:00","2018-01-01 04:00:00"],
		"texts": ["HY7z5", "Bqg3a5HE9bZRS2eXCF5t", "PbjBzxilXwxoXGBW1JDz","KkCA4YRzMhctaWAZ5", "6B5b0YcBYqcdlkRFo"],
		"checksummd5": ["379fb587cd514ec2f9576d728aaa5d50", "57934db7336d3de928f125504babe08a", "6fbdc7deb426131dda83b689d8372ed8", "4c6e11af62414cade90412a292033765", "e6932d483223274bee38f96c2af427be"],
		"checksumsha1": ["8b54cee01a6061f2578bb995ca7e956102399fc5", "7a98122912aeedfc09f9843eaad5a29713235d71", "e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d", "ad1cec36b81a89418bbfde3b0d3c240032d3bfe3", "31f9858365b89a683aed53c94839742928eb1028"],
		"bools": [True, True, False, True, False],
		"hugeints": [37602, 82645, -74956, -80508, -78726]
		}

	return pd.DataFrame(data)


def data_30():
	data={
		"seq_num": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
		"float": [0.000000, 0.344828, 0.689655, 1.034483, 1.379310, 1.724138, 2.068966, 2.413793, 2.758621, 3.103448, 3.448276, 3.793103, 4.137931, 4.482759, 4.827586, 5.172414, 5.517241, 5.862069, 6.206897, 6.551724, 6.896552, 7.241379, 7.586207, 7.931034, 8.275862, 8.620690, 8.965517, 9.310345, 9.655172, 10.000000],
		"float_neg": [-10.000000, -9.655172, -9.310345, -8.965517, -8.620690, -8.275862, -7.931034, -7.586207, -7.241379, -6.896552, -6.551724, -6.206897, -5.862069, -5.517241, -5.172414, -4.827586, -4.482759, -4.137931, -3.793103, -3.448276, -3.103448, -2.758621, -2.413793, -2.068966, -1.724138, -1.379310, -1.034483, -0.689655, -0.344828,  0.000000],
		"random": [0.469527, 0.104732, 0.975000, 0.349125, 0.124884, 0.248686, 0.669628, 0.516864, 0.274127, 0.616159, 0.832415, 0.647618, 0.998046, 0.612735, 0.042850, 0.600995, 0.925378, 0.294278, 0.417281, 0.012734, 0.327652, 0.685694, 0.861183, 0.454704, 0.445780, 0.570922, 0.619044, 0.921637, 0.588431, 0.301596],
		"dates": ["2018-01-01","2018-01-02","2018-01-03","2018-01-04","2018-01-05","2018-01-06","2018-01-07","2018-01-08","2018-01-09","2018-01-10","2018-01-11","2018-01-12","2018-01-13","2018-01-14","2018-01-15","2018-01-16","2018-01-17","2018-01-18","2018-01-19","2018-01-20","2018-01-21","2018-01-22","2018-01-23","2018-01-24","2018-01-25","2018-01-26","2018-01-27","2018-01-28","2018-01-29","2018-01-30"],
		"datetimes": ["2018-01-01 00:00:00","2018-01-01 01:00:00","2018-01-01 02:00:00","2018-01-01 03:00:00","2018-01-01 04:00:00","2018-01-01 05:00:00","2018-01-01 06:00:00","2018-01-01 07:00:00","2018-01-01 08:00:00","2018-01-01 09:00:00","2018-01-01 10:00:00","2018-01-01 11:00:00","2018-01-01 12:00:00","2018-01-01 13:00:00","2018-01-01 14:00:00","2018-01-01 15:00:00","2018-01-01 16:00:00","2018-01-01 17:00:00","2018-01-01 18:00:00","2018-01-01 19:00:00","2018-01-01 20:00:00","2018-01-01 21:00:00","2018-01-01 22:00:00","2018-01-01 23:00:00","2018-01-02 00:00:00","2018-01-02 01:00:00","2018-01-02 02:00:00","2018-01-02 03:00:00","2018-01-02 04:00:00","2018-01-02 05:00:00"],
		"texts": ["HY7z5","K2ZyI", "bCubr", "PAtVD", "2xc6A", "EdCGG", "b6xE3", "WhHq8", "odfYX", "PKvFc", "Bqg3a5HE9bZRS2eXCF5t", "PbjBzxilXwxoXGBW1JDz", "Jlwo2DMiFmcPCGHSzwVE", "xfX8VkvOcLZwyBCxC53a", "O6D9qIykq8RS2mmJSiZ5", "8r8WP5LEA86FvCxiD5QU", "gbbVQN4Gj236ebsv7K8y", "0h13KQdGUArlIINxw9UQ", "z0SZSxl2WGzrOH0jaHSG", "QUowCxp1bQ8Q36SmJOEP", "hAxx8aYcD3h4C4d6L", "Z46ocC9wOFjZy1yaq", "5M0RZ9TQLly7o5KYO", "fRr1jqjKCrYznmwSq", "N4XaeFH4wz6CVAOua", "UdNGrHKr8ZdDIl2Fz", "yemH8vpttob3EenfB", "l7Wtk4Bd5ZOi6LhMD", "KkCA4YRzMhctaWAZ5", "6B5b0YcBYqcdlkRFo"],
		"checksummd5": ["379fb587cd514ec2f9576d728aaa5d50", "57934db7336d3de928f125504babe08a", "6fbdc7deb426131dda83b689d8372ed8", "4c6e11af62414cade90412a292033765", "e6932d483223274bee38f96c2af427be", "dd61850fc5610f3af21f762fdb5ea592", "5c2967aa26bcb978c2e9d825fcb28d3d", "47fd298fc9480f33f9e49a91478f5568", "3294f2452d19361e8b1e6a18e092115f", "ac27077346d5b8e5d0e7211e70a8a72a", "8c7e72a4679d46ddfc2cb875b97be959", "6ea14aca30455e407d32e2abf68709c2", "e6c02729595f0e2d6de781ff589771c7", "7452f9447f0543339c4962c606c98cb8", "b270766edd5749573ed9c94129443cbc", "aa23a015b7d20e7270b4371c10abc46f", "12e651911a19b5c194ef9da18b36b416", "fb85b8cd546f3ad2db6f0ce455ba21ae", "76316dd0e58a51e0ba3e8609747b488f", "98fb966dc9bf12e6c54d9ae3b004f80f", "18261dbfd9f3307d58b799c6f96dd754", "96621689eb283a9f33e9d8ce6adb5e15", "20c0958030fc6084471a08288fca6c61", "ec28983fc697fb1c4b43f33fb9b0be4e", "1f097a0cc97061b0c9f1cfe93426eb5c", "96b1e315809f97bba7928785e0057b5e", "a59a8371bb95174141eff9b64baca231", "3b9fa861ebff9367a3e8c420f9f68ea7", "b99fc6fc0406df9e12917e09a02b6e39", "98360bc0d82c95975bc20d701c287d24"],
		"checksumsha1": ["8b54cee01a6061f2578bb995ca7e956102399fc5", "7a98122912aeedfc09f9843eaad5a29713235d71", "e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d", "ad1cec36b81a89418bbfde3b0d3c240032d3bfe3", "31f9858365b89a683aed53c94839742928eb1028", "0f0ae0a8ce380385c409bb4dd4539d9eb0d270e5", "d7cf42daf12facdcaf0d4401af6804a671349497", "cf8ab9e2c79bf444ae598a69a3d0da30260e52a9", "034fe4e8c5502db785a89cf619e007b8d948d415", "8da8494375ea54029301b347fb6cf25c9191c96d", "22df42ad603d769a814386edeb18cfb682a8c5ac", "4c9b2f06a8d6acd0ec7d8efa493cfe6f9a72625b", "86664416bc03cd32c239ab213042c1bfbf973694", "754863da0ca4b29859fcc8302860b4a15b7897ef", "1d200a7894770a85f9cb0bbe747c831076d127ff", "1d4dd40b5dc5f6109e7706ac5d91f0af6d61b035", "9085089ead4965f588f46fb8d4d13c5a8c2a01c4", "9561847740ec2fc97e80081a4d2ac8bfdddcbb3f", "0b15a498096fbc94e2f74871b13396590936e3e5", "a35fbb08a474fc708f918c1fe4fe8fa9014ad22a", "b92571189160b4dd49cd115da6a34b5faeb23bed", "ea109cd5bda401b90eabd8a4abc5053c25dff0d4", "052a7aa5d7c015fd50a3ff893397fd37afade29c", "a64913c5ee7e47a3cee2da8dc9293108051a252d", "25f42dc02922e8d261c6f0f380d270159553e8e8", "5abd7e0b9884a63601802a28d0d8c1aaecbdd9de", "85f4e0669e995c17f883244c13d490b71e8cd163", "65595aa94c3e1d7ed7e9872a0870c8cbdcad7421", "05d2c16c7a8d2f7e90091b0f462b5c502470317b", "c7dc9ad0642b5d4c6811f5d1a245f6344a28a8ab"],
		"bools": [True, True,False, True,False, True,False, True, True, True, True, True,False, True, True, True,False, True, True,False, True,False, True, True, True,False,False,False,False, True],
		"hugeints": [37602, 82645, -74956, -80508, -78726, 55994, -87590, 84084, 81114, -28833, 402, 3790, 50257, 6060, -12159, -7401, -95666, 801, 69048, -63518, -64763, -54385, 32177, 27145, 7991, 66414, -57811, -73799, -69715, 71227]
		}

	return pd.DataFrame(data)


def data_100():
	data = {
		"seq_num": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], 
		"float": [0.000000, 0.101010, 0.202020, 0.303030, 0.404040, 0.505051, 0.606061, 0.707071, 0.808081, 0.909091, 1.010101, 1.111111, 1.212121, 1.313131, 1.414141, 1.515152, 1.616162, 1.717172, 1.818182, 1.919192, 2.020202, 2.121212, 2.222222, 2.323232, 2.424242, 2.525253, 2.626263, 2.727273, 2.828283, 2.929293, 3.030303, 3.131313, 3.232323, 3.333333, 3.434343, 3.535354, 3.636364, 3.737374, 3.838384, 3.939394, 4.040404, 4.141414, 4.242424, 4.343434, 4.444444, 4.545455, 4.646465, 4.747475, 4.848485, 4.949495, 5.050505, 5.151515, 5.252525, 5.353535, 5.454545, 5.555556, 5.656566, 5.757576, 5.858586, 5.959596, 6.060606, 6.161616, 6.262626, 6.363636, 6.464646, 6.565657, 6.666667, 6.767677, 6.868687, 6.969697, 7.070707, 7.171717, 7.272727, 7.373737, 7.474747, 7.575758, 7.676768, 7.777778, 7.878788, 7.979798, 8.080808, 8.181818, 8.282828, 8.383838, 8.484848, 8.585859, 8.686869, 8.787879, 8.888889, 8.989899, 9.090909, 9.191919, 9.292929, 9.393939, 9.494949, 9.595960, 9.696970, 9.797980, 9.898990, 10.000000], 
		"float_neg": [-10.000000, -9.898990, -9.797980, -9.696970, -9.595960, -9.494949, -9.393939, -9.292929, -9.191919, -9.090909, -8.989899, -8.888889, -8.787879, -8.686869, -8.585859, -8.484848, -8.383838, -8.282828, -8.181818, -8.080808, -7.979798, -7.878788, -7.777778, -7.676768, -7.575758, -7.474747, -7.373737, -7.272727, -7.171717, -7.070707, -6.969697, -6.868687, -6.767677, -6.666667, -6.565657, -6.464646, -6.363636, -6.262626, -6.161616, -6.060606, -5.959596, -5.858586, -5.757576, -5.656566, -5.555556, -5.454545, -5.353535, -5.252525, -5.151515, -5.050505, -4.949495, -4.848485, -4.747475, -4.646465, -4.545455, -4.444444, -4.343434, -4.242424, -4.141414, -4.040404, -3.939394, -3.838384, -3.737374, -3.636364, -3.535354, -3.434343, -3.333333, -3.232323, -3.131313, -3.030303, -2.929293, -2.828283, -2.727273, -2.626263, -2.525253, -2.424242, -2.323232, -2.222222, -2.121212, -2.020202, -1.919192, -1.818182, -1.717172, -1.616162, -1.515152, -1.414141, -1.313131, -1.212121, -1.111111, -1.010101, -0.909091, -0.808081, -0.707071, -0.606061, -0.505051, -0.404040, -0.303030, -0.202020, -0.101010, 0.000000], 
		"random": [0.933617, 0.600065, 0.741727, 0.014468, 0.691504, 0.673325, 0.911767, 0.996944, 0.932610, 0.187280, 0.147329, 0.558328, 0.812202, 0.446925, 0.369438, 0.608076, 0.765427, 0.139518, 0.373653, 0.850819, 0.236784, 0.867821, 0.457112, 0.058699, 0.941723, 0.189632, 0.983689, 0.618842, 0.509341, 0.938231, 0.137581, 0.316464, 0.351173, 0.705978, 0.320338, 0.257642, 0.658705, 0.135605, 0.729063, 0.511917, 0.491550, 0.372146, 0.451885, 0.168600, 0.563395, 0.818014, 0.838983, 0.871263, 0.734803, 0.744895, 0.358297, 0.439853, 0.051245, 0.273719, 0.438941, 0.477490, 0.225039, 0.519368, 0.257968, 0.104132, 0.636296, 0.809199, 0.361650, 0.993855, 0.786564, 0.824094, 0.096985, 0.925626, 0.553405, 0.634690, 0.449240, 0.308730, 0.125726, 0.082594, 0.964324, 0.169631, 0.617983, 0.800686, 0.149389, 0.490352, 0.448164, 0.499737, 0.987062, 0.793639, 0.712315, 0.038103, 0.796980, 0.701092, 0.879729, 0.803986, 0.995120, 0.365850, 0.573236, 0.231645, 0.992325, 0.542323, 0.960158, 0.344509, 0.400841, 0.415775], 
		"dates": ["2018-01-01", "2018-01-02", "2018-01-03", "2018-01-04", "2018-01-05", "2018-01-06", "2018-01-07", "2018-01-08", "2018-01-09", "2018-01-10", "2018-01-11", "2018-01-12", "2018-01-13", "2018-01-14", "2018-01-15", "2018-01-16", "2018-01-17", "2018-01-18", "2018-01-19", "2018-01-20", "2018-01-21", "2018-01-22", "2018-01-23", "2018-01-24", "2018-01-25", "2018-01-26", "2018-01-27", "2018-01-28", "2018-01-29", "2018-01-30", "2018-01-31", "2018-02-01", "2018-02-02", "2018-02-03", "2018-02-04", "2018-02-05", "2018-02-06", "2018-02-07", "2018-02-08", "2018-02-09", "2018-02-10", "2018-02-11", "2018-02-12", "2018-02-13", "2018-02-14", "2018-02-15", "2018-02-16", "2018-02-17", "2018-02-18", "2018-02-19", "2018-02-20", "2018-02-21", "2018-02-22", "2018-02-23", "2018-02-24", "2018-02-25", "2018-02-26", "2018-02-27", "2018-02-28", "2018-03-01", "2018-03-02", "2018-03-03", "2018-03-04", "2018-03-05", "2018-03-06", "2018-03-07", "2018-03-08", "2018-03-09", "2018-03-10", "2018-03-11", "2018-03-12", "2018-03-13", "2018-03-14", "2018-03-15", "2018-03-16", "2018-03-17", "2018-03-18", "2018-03-19", "2018-03-20", "2018-03-21", "2018-03-22", "2018-03-23", "2018-03-24", "2018-03-25", "2018-03-26", "2018-03-27", "2018-03-28", "2018-03-29", "2018-03-30", "2018-03-31", "2018-04-01", "2018-04-02", "2018-04-03", "2018-04-04", "2018-04-05", "2018-04-06", "2018-04-07", "2018-04-08", "2018-04-09", "2018-04-10"], 
		"datetimes": ["2018-01-01 00:00:00", "2018-01-01 01:00:00", "2018-01-01 02:00:00", "2018-01-01 03:00:00", "2018-01-01 04:00:00", "2018-01-01 05:00:00", "2018-01-01 06:00:00", "2018-01-01 07:00:00", "2018-01-01 08:00:00", "2018-01-01 09:00:00", "2018-01-01 10:00:00", "2018-01-01 11:00:00", "2018-01-01 12:00:00", "2018-01-01 13:00:00", "2018-01-01 14:00:00", "2018-01-01 15:00:00", "2018-01-01 16:00:00", "2018-01-01 17:00:00", "2018-01-01 18:00:00", "2018-01-01 19:00:00", "2018-01-01 20:00:00", "2018-01-01 21:00:00", "2018-01-01 22:00:00", "2018-01-01 23:00:00", "2018-01-02 00:00:00", "2018-01-02 01:00:00", "2018-01-02 02:00:00", "2018-01-02 03:00:00", "2018-01-02 04:00:00", "2018-01-02 05:00:00", "2018-01-02 06:00:00", "2018-01-02 07:00:00", "2018-01-02 08:00:00", "2018-01-02 09:00:00", "2018-01-02 10:00:00", "2018-01-02 11:00:00", "2018-01-02 12:00:00", "2018-01-02 13:00:00", "2018-01-02 14:00:00", "2018-01-02 15:00:00", "2018-01-02 16:00:00", "2018-01-02 17:00:00", "2018-01-02 18:00:00", "2018-01-02 19:00:00", "2018-01-02 20:00:00", "2018-01-02 21:00:00", "2018-01-02 22:00:00", "2018-01-02 23:00:00", "2018-01-03 00:00:00", "2018-01-03 01:00:00", "2018-01-03 02:00:00", "2018-01-03 03:00:00", "2018-01-03 04:00:00", "2018-01-03 05:00:00", "2018-01-03 06:00:00", "2018-01-03 07:00:00", "2018-01-03 08:00:00", "2018-01-03 09:00:00", "2018-01-03 10:00:00", "2018-01-03 11:00:00", "2018-01-03 12:00:00", "2018-01-03 13:00:00", "2018-01-03 14:00:00", "2018-01-03 15:00:00", "2018-01-03 16:00:00", "2018-01-03 17:00:00", "2018-01-03 18:00:00", "2018-01-03 19:00:00", "2018-01-03 20:00:00", "2018-01-03 21:00:00", "2018-01-03 22:00:00", "2018-01-03 23:00:00", "2018-01-04 00:00:00", "2018-01-04 01:00:00", "2018-01-04 02:00:00", "2018-01-04 03:00:00", "2018-01-04 04:00:00", "2018-01-04 05:00:00", "2018-01-04 06:00:00", "2018-01-04 07:00:00", "2018-01-04 08:00:00", "2018-01-04 09:00:00", "2018-01-04 10:00:00", "2018-01-04 11:00:00", "2018-01-04 12:00:00", "2018-01-04 13:00:00", "2018-01-04 14:00:00", "2018-01-04 15:00:00", "2018-01-04 16:00:00", "2018-01-04 17:00:00", "2018-01-04 18:00:00", "2018-01-04 19:00:00", "2018-01-04 20:00:00", "2018-01-04 21:00:00", "2018-01-04 22:00:00", "2018-01-04 23:00:00", "2018-01-05 00:00:00", "2018-01-05 01:00:00", "2018-01-05 02:00:00", "2018-01-05 03:00:00"], 
		"texts": ["LaWvs", "aSiqq", "pwKi3", "CWcqA", "ELLN1", "ODz2m", "aPW0E", "edqz0", "tmOgG", "lkdjG", "Wk6lp", "4kqBg", "CUtii", "3GiXY", "2Hx97", "GwMHs", "Wcte0", "jgrPi", "SZMdL", "FjU5B", "8lMvs", "FPKq5", "0JeuF", "CizGn", "yJQGX", "E56Aay4E76BFNdXW74oZ", "78MemKYnAA4HX3beAFrZ", "lPCiTRvgEhoi6w0740hb", "xu7LGIxn7iGy1ytFSJAX", "kQgeo46rpp958GOMjEnf", "OnPxcq94OdUQPC66gZTz", "VzMsp2Nmo4iGpGKmInkr", "9BU7KcZKWsyn3i5Q7Pzp", "DYpQyyrTt84HINdXTxeJ", "5wrqPbhqGpVQnR5bNbcR", "ZxdrRe9R8AwC2E5wNyP7", "QBBiGb5pYFFhJy4N2UJ3", "YKxVDECwgHqS628qvhZX", "dTnJY3VRo3qkOYc6NKVR", "ZXWAIIzk4TQyZJb1v06u", "uLw2qekxWzZDrVTJaJM1", "ms5uW63EwnwiRiXuq1Zg", "IonHqcYEWNziFnLT4mU6", "X3naDwSWaveQ7vPRAp6l", "glLMdBfIOcPNRX0pFp5G", "LM15hT4pcGM5ib7yIiNE", "Nt7H20Exn15Kgi2xoAef", "mg6aQLraMM3nZkVI6Z7e", "4H64J64itWqv0H01SvQX", "brbmV6CFSuLmgpnH3YBk", "F75hKD3At3p8NPVXi", "q0ObMKBxVApy1zyFs", "WD8cjJuiQuWaUMw1Z", "byO1RJYAMnwEKSJ1y", "tf2basyUh8M3qFMjc", "d7X7FcytYZ70kzbyz", "skZ8yHe23JvJmRygg", "5lnEe0phGqiTtPO6a", "7IM5fSwekCfA4M2De", "wkVtsahe1iv3o8o9R", "3x671VnqWAcwUiTMO", "1nj2eqr1vjQQuJ3fJ", "eclxWy38ETT1kNfxC", "MHm9MHZkRADRMySkA", "a4Bke2JweCpg6BcKi", "AKVIhQ0HLBOBduM7o", "NKWo0FgydosQBtdTt", "t4K98jCbdMo5q4AnY", "szeIS0bBc312JILGZ", "0KyuDWD4LIAlsPI49", "TyQmW63gNAAFf75QE", "Bg4rWKu7IjLcVMdTq", "7r4acWdu1L4rHJKVC", "XCRSFxO6s05oG7JpN", "D4q62Tx3xOCe2G6OD", "IV3hcDf0NwUPOCd76tU5tt", "hWD9XTmBtYthyKg4sQL1yB", "nv9tEfm0nVB9JGlp0STqPn", "NS5NFQhguCkzZe5YgBuIV1", "fgHF1NAMwX6Z335pbp4SSe", "QJWNcaQ3pwDwRvzZeQbC3c", "EpgeAAESCUIwwGMUKaYhdA", "3JkuEhhfinm1YPzEF0LmMt", "WfMk3BwGbset2jXHfRWPtq", "RZdEEBRZ7jdztpQOXqSOxA", "3B8MhPWWW7s67TGViHkqS1", "47Wgssf3EwTAFiKpiNThQc", "OklRVa1OiDjQo2zVOxtWZY", "rUD3JeyMRPvgvKFY8mXGbS", "ubjK3EETSZ8CClgcJFQmht", "psfdoIDCBOuOQ69dCBtVky", "vx0W6UoZmlwIeyWcSiAhY1", "tu9zjCx1Lb7QJnzC9x3tbU", "qB6WXeMXQy4snyjHkN8Pq2", "EazU4MkTMSoUPTMdiIZNG4", "8WxkahOj8X0MyMGi6bN7Ca", "tprsDjMzTiyL8ZLH8cJeW5", "mzLe23aFAeJW8OWUkuaBHs", "AiC5POZKwu5TLOl2sieYgV", "UmsJ4Cx4JEixQbLlz3Uava"], 
		"checksummd5": ["f8d29ac934477a1bfdfc052ce3ea72b6", "63a2d2467d98a7129921190b6584e7fe", "0586d895c97042a543772cb1a0810ac2", "2ca3c7c55adb3295f2134502de3a586b", "662046d7f1e6410b01f93291c3010750", "19eddf04435ee64d1303c51eb32be95a", "3af9a2031cb8b3bbd83fc4352636fa6b", "d1d4d3b9754d74116f1df06cd4b46022", "61268332fc90598b3d0fdd570d232dbf", "a537913f51be234a055bf91dc6903ba3", "ae5d053d38ee1c34d9271caf4026f42d", "a4a1540dbccb2e1d015bacabad9ce70e", "69bf597964768dd179f89c5446cac17c", "ea180235fa99bd3eede88ef7f8dce94f", "f8553542034128c90e169b0b1da36b5f", "478083037d5a0cca4fdb71de5f5338b6", "541ba5571d3f7f2a251521c27b778d01", "16372fb4d732862650b7231063fc30a7", "cd540fc27e03ee8ecaea210cd6011d0c", "78fb095f56b4357b0c39fccd94e004ef", "2ea64a26850dc3751114111f486de269", "70485201d0283a519323627324fa04d7", "7363ca3edf9964a559efeda99f80a9ce", "382bf51e955f3ebf6c2ddaaba221ddb8", "0dccc6dd6aead6773ddb7b5f47142ef9", "012b559a0f047943d0b59d22f742b482", "09d3cd6eb93bcda671260b4f4a53e802", "c3023d945e9d3ac720a8afbfcd68462d", "145d900e70f6289bc045997a4e62d4b8", "87be23ed1976257eff566d260dd4dfb0", "7e0376e4412c85aa4428973a02a378c3", "97887863933a8f1428d5e2d26f25f24e", "1c022b82c73e8d39af4711197e78dd82", "294dfdaa0e7327bf2713c61619314cd8", "a5ccf0d925074053f63249e72f1d97f1", "cbfd4f3b597ec15908f5402c66b846c7", "9ef4fbd05395fbe58c7595e2a547cf53", "fee779d98e8d0dc6db8b051910272f84", "cdaaccec99827e006467fd7a8489528a", "94f953b9f83418732d13b6b815dc8eef", "932951290b6971be1583ee203fc3b42f", "5dfeda2b6e510c8e00196e871e40c59a", "c69708471568d836ea9ae5afd2c99497", "c8413aa1f7e966bfcb202249e608dd35", "cd5f2191c9bc23deefcb5eb00487b900", "c64c1448ed2e88959b1da053dc53e907", "c51be9a6f4c2ba644f2ccfda189cf4d2", "88e153c43ac7523aa1a5a83ade45455c", "f6c40fffbadf13ecc9d3d8fbc47f68aa", "1f4450186cf25a520bede3641bae7b3d", "d243f671b4509daee7ea58131421c087", "1781f2d9fd285483db17e81343fbc6d7", "0e204df650a4710a9a3d234f45eddbb4", "cec85b56d8999764d32c2219a976346e", "006a0f82e0c4887b4f8fcc484cdfb95b", "d050e50e4cfc9663a96cee7e11449b46", "5059c644195a6a3735ee297694fd87e6", "11aa1e56274bed09401206a3cece1e5c", "82e10f04ff4801d9e8d372ae97020652", "10fc1c366901025364748fb2ba1c3b39", "9ff3c574f3d2709739870eecd6f65edb", "fa91fe15f9bfe7658b0ccb72eeb2f886", "44268c21e5522534d538e7317edd861c", "16d9143d67aef2390469a15c367690f3", "93604b839002f66df61be3a1325cf934", "3b737a93c08c79e87cfe6978d71478dc", "ae852ad224fd6ab081b24fe4672d4ba7", "f00f4cfacf2183741877520352a0681b", "0a1fcd746ef49fdccd0fceb344e5bcfe", "ebd5a72ac99fe328ff514421bab79e3d", "d306ddf25511b2ff605ad705054a418d", "39c875142a8d0d658ea49346c6687a75", "1c053f53f2fb50c9e5ed402c651737f0", "82fc5986f116de5365e1a48914397d79", "116bead927db52f0de8e634fa53f595f", "2beb7d6935652cbd2da814251805091e", "9136cc1d6390aeced3952133fd25fbca", "812c447d0851b56f1c8fa2d52ab79cd0", "4c1dbf6f199d42ed90d9042a78a1e939", "143ce6a0c00fb46530d83acdc251fb20", "057555fd97ac91cc4a604c7e488d41cb", "479691fcc006e6a48c98a4b853e09322", "4b963039a638b3a1a075dac68c5e6134", "bdb879b5611a999f838d8d7b1918351f", "48b53470339b70d10edd93f26b002e6a", "df783f852b092091deab1ebdddcd0bfa", "2148a059fb5cab22254f6170a8a09b13", "b19e7376b36626bc989a6a956e0a6158", "ffb84f864398e4d7341d57e3092c4f25", "585319cfb37bf967fc19c51213ee8c39", "701e4a9a18856a05a76f313ff308f09c", "0c2e4c3908f4821033ce0763097b0b4f", "2dfbb261755e93a40e165aef272edfad", "9d524e81e226698d42ccc91aac8fbee7", "c8c31b8b322a0e284a21862ce6e4ad18", "ddd6b7462477400ec521d4c978f927de", "5d9a47ea2aed57c143ab053e5466dbfd", "ad342d2f900b41a01c20ea8457c441af", "e96bd39eebde5c353884f4345ba5416e", "7f496164910235a69c3ed45190c52d0a"], 
		"checksumsha1": ["5aa8804b1fa6db46b286c504c6c38411d50408d1", "e6c2275188a77764a747467e178bc193a725d3ad", "5ac130d0e138a5d74c29ff36ba3a6b1f27b344f6", "7e15d5a9b17da9357822015ac458eae100c0f06f", "ce7fe4c68d6dc7324ac27c96a83e0aa9685598af", "683366487067e3d0c36ff9cf85b716437b730af1", "6b1fbf434e925cec851c004095d4e6c97d575c90", "2a95cc68ba5e0194586a3eb71190cc295b12ead1", "28933dbfe81beeac504632c48a1a6a0eebaf36c5", "380e73cf636ed4cf6b90c45e90108b873256143e", "91e53704bf1adc174fa4cd111d255b9643a69098", "43fc1bc9a59ab36b4b47a62db07cee880fbea537", "5ae1a7a5432697d82f5e39f14c8d47acc982ebb6", "aeafd23e4fe4071d1cd507145ec2454b4f8cd99b", "2e62daf4bcc57e080cd0ad615c3acd70b3d9585d", "3c24d0463b2293ad3021ecd363f31c1baf87dfd1", "84aab2ab6f764121ab89df424139e9c088375fcf", "d15a48e3d295caf53a5746fa5d5b6b352e8217e0", "9b5021af1209eac979f5338dd1632b07d4293268", "3971a212cc469d01c851393864ae3223bdbf509f", "44a0fe7c9725ad6cb3eedfe62bc8ca25970822db", "341f6f536d47b6f9bed6196eaeb87558384c34c7", "42b7d364bc860b3bbcb1bc3ff17c13fcf6f37c70", "d90bcf719190387d290b3ec17215d435e4ddd881", "8330be8feff684f42e7dd63923854fcd1603ccee", "2e37e61ef14525acc259f971b1aa774cb2d40c5e", "f1fd38ac83075297b6445205c895f62036646c77", "74ae3c55c89444ec7e4610660584ec9d00a14fba", "9ba1df3a8886d356c1556177e0e3ef0f4c0fe492", "f33f251b4d3e48909093bfb60c934b0f25d16526", "f56a5833ed23e0c446b4096759b158fa6eb75919", "31063bdd430f244b554eb00f82526cccfdce1b8c", "b59f8ebca8e1bf8cf4b8d4366510592613d5fa3d", "3d5153911801e59763368614b270e4df9c161ad7", "9cdc4bcbbb1f7c6773c21b05ed867494d98640c4", "0ce7ad6e3ed759c3ee73c7241243fa6195e42e9d", "58954add6a43188efefad7c9e5941adddb217faf", "fa4114803cb4d2ec2ef86f9f195368ca9f21e771", "131a10a95ebfb1fc6b7b1342e3aba69766e1ccc4", "de2671ee82ecffcdeec8290ff22beefb6bbda143", "e8fa8af2fbe73796162ef36587834a1e337f4a28", "40d153fe9ec21596a8e33b4362243ab17dd3a4a1", "db83b0b0ae945d36bb4426b2fa83612e08d2eca2", "e86e7d182d8e329faf8cff5969c942a57a65b505", "d2396144db92bd09b9f56928d15607cf5f6d79e1", "7d584181f9d1e7a1772727b6cca4d008ab1b2313", "3c1067668ed34eaa1317d9422c4dc71aa0fb60df", "46f542a62de090dabf83abe0b37b60fd0a85aec6", "b893231db8ded48e2df3cfb4b2205562e4f12246", "3b5fbabe594c92fbfb5170cc9439fa56fbea11ef", "f7f298b5465606cde9b9d4da107e46dce3c60dbc", "2c9bf37bd7deeddecca65a3be3b41a59c45bbd52", "be66c4250858acb9af59352233bfebf3f59ac810", "83c07ed5cc0c81803684a91f392b63919cb6f1ff", "221302390b7ccc1f59e52a119cf0d5d80ff09555", "d36f66b9c55ba50d44833c47bc7a87c3d0ac1940", "f44ad384ada49ebeaea0644de4b159999c69c65f", "4937b280558bf6be96008abcbfb3f20983ab361b", "f6cbb6e209f7fc337d57756cef755bf2abe3f957", "5007506087b016cda2edff389077eb2721d1ac28", "ac4257b1a72bb8b82a066747185dfbacb3b7c47e", "2990df42300c30ce49cb79ba6bf60ddabefb680e", "bf16b1816c87894b37a9d592af3a007fcdf22dba", "49234ecb671fb277ba692438ad0e4d1062310df5", "7a829e48f568f2abf2ecfcdc60833ac077f89940", "72e1425b87097eed9320b9a146e9f6580126a786", "d0ed69be11ca7cce416345ab5527f4e703dbe7bf", "091094cda811b28452bba8ce951cbf943754d858", "36d32c79046e42543869cb49951683c39069f645", "a3e62e48d27b7705b78163dad1101e129fe2e2f0", "e8409f90d1b326720e9d01837f94c9d5ee18c579", "f6f9c5a3ee6708b9cc7c1c07d2337aafd1a52d0d", "ec4fcf9c49140194508f14a22d51ee0586cf21dc", "39949c56fc82c4a29f4696371184b292bd72557d", "233a12946331c626e583621dacd86b85c0fd9461", "428ca79d82ed84f14410b3b3a54de14c8ce38eae", "f6bb4bedc9967136a161c795ea6ef94341ee0d99", "86c0cbe5cc6ea040ef5d9413383b386ef03137ec", "8bcb2eb31949625ab11ba3fe23cf63a87d161498", "825f3fd7e72297b9634012ebc36a75474e3a104a", "84d80c3d03a94bafbdab871c1ec8004a4c59a3b1", "ee736a24c525a8d264aed2f1c17d9d50c1e13612", "67cac17440d3526896df6efdd511658762dfb607", "91a913e2d5309e29c630773ad6eb0058b6352e50", "c3ec54f118a1038661d0bbde31ae0f6fa2a5db13", "d3331f5d85d677553f9f0369dcba57e55c0c2267", "a6daf8ffe673557960cb0835ee6ff6f8c295ac4e", "55d52f684a3bc76cf45a6f06ff799bd7de8e8289", "30400d98e5635da655df1fd991a84d08e9e3c694", "0f470e27e3db47158fca315b6e0e2d6339ca0c72", "cf5a71438879fd5bbde5e760f687af6dc54485b3", "f2341a3c28a6c5bf1672b0fa970969360ae540e1", "ead5c058b497bbe84c4a5b5334c2d7c444e562c3", "c2b5f6ecfddcfec81c7b7422437713bfed9040a1", "fb715ee51589acd11cd4fafaa7e789bba8faede2", "ed143f8d3d47eca4aa04db99cb4c0ddcbd1a5747", "9a0fbd7ac83bbb4f2087d2a97ee4abe7dc24341f", "0831d9c9e197e674be920bd39bc74653ca05b138", "30ba29e5a28e0050b0a9b8b6e6a3a263167f22df", "2a347071b0199e7f11958c73832f107f7716eeba"], 
		"bools": [True, True, False, True, True, False, False, True, True, True, False, True, True, True, False, True, True, False, False, True, True, True, True, True, False, False, True, True, False, False, True, False, False, False, True, True, True, False, False, True, True, False, True, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, True, False, True, False, True, True, True, True, False, False, True, True, False, False, True, False, True, True, False, True, True, False, False, True, False, True, False, False, True, False, True, False, False, True, False, False, True, True, False, False, True, True], 
		"hugeints": [-6217, 92153, 42474, -59704, -79214, 57258, -23922, 62425, -91925, 3039, 38689, 96559, -76221, -35067, 53638, -30391, 6659, 58069, -31947, 82380, 8490, -17006, 71340, -74211, 51539, -62939, -19086, 86826, 69242, -46350, -77260, 661, -95006, 22299, -89082, -85258, -23737, -56992, -90898, 41051, -22209, 6922, -8325, -15755, -29116, 29798, -98586, -3017, -51806, -8598, -81341, 29883, -20565, 33204, -17302, 48925, -97039, -67869, -91837, -84194, 99419, 58482, 30004, -23685, 73718, 18137, -37778, -66310, -93098, 21285, -89262, -68908, -93611, -42664, -82581, 58999, -23387, 65441, -71733, 95759, 41231, 43992, -23337, 36359, 91431, 10270, -14607, -924, -33561, 16, 8010, -90220, 86486, 90319, -23083, 32672, -24878, 14742, 94049, -14262]
	}

	return pd.DataFrame(data)

def test_slice_data():

	renderer = PandasRenderer(data_tiny(), preinit=False)

	result = renderer.slice_data(0, 4, inplace=False)
	assert result.shape == (4, 11)
	assert np.all(np.equal(result.values, data_tiny().values[0:4]))
	assert renderer.data_slice is None
	result = renderer.slice_data(1, 4, inplace=False)
	assert result.shape == (4, 11)
	assert np.all(np.equal(result.values, data_tiny().values[1:5]))
	assert renderer.data_slice is None
	result = renderer.slice_data(0, 3, inplace=False)
	assert result.shape == (3, 11)
	assert np.all(np.equal(result.values, data_tiny().values[0:3]))
	assert renderer.data_slice is None
	result = renderer.slice_data(2, 3, inplace=False)
	assert result.shape == (3, 11)
	assert np.all(np.equal(result.values, data_tiny().values[2:5]))
	assert renderer.data_slice is None
	result = renderer.slice_data(3, 3, inplace=False)
	assert result.shape == (2, 11)
	assert np.all(np.equal(result.values, data_tiny().values[3:5]))
	assert renderer.data_slice is None
	result = renderer.slice_data(4, 3, inplace=False)
	assert result.shape == (1, 11)
	assert np.all(np.equal(result.values, data_tiny().values[4:5]))
	assert renderer.data_slice is None

def test_calc_column_sizes():
	renderer = PandasRenderer(data_tiny(), preinit=False)

	data_slice = renderer.slice_data(0, 4, inplace=False)
	result = renderer.calc_column_sizes(data_slice, inplace=False)
	col_str, col_minsizes, col_maxsizes = result

	expected_json = '{"seq_num":{"0":"0","1":"1","2":"2","3":"3"},\
					"float":{"0":"0.0","1":"0.344828","2":"0.689655","3":"1.034483"},\
					"float_neg":{"0":"-10.0","1":"-9.655172","2":"-9.310345","3":"-8.965517"},\
					"random":{"0":"0.469527","1":"0.104732","2":"0.975","3":"0.349125"},\
					"dates":{"0":"2018-01-01","1":"2018-01-02","2":"2018-01-03","3":"2018-01-04"},\
					"datetimes":{"0":"2018-01-01 00:00:00","1":"2018-01-01 01:00:00","2":"2018-01-01 02:00:00","3":"2018-01-01 03:00:00"},\
					"texts":{"0":"HY7z5","1":"Bqg3a5HE9bZRS2eXCF5t","2":"PbjBzxilXwxoXGBW1JDz","3":"KkCA4YRzMhctaWAZ5"},\
					"checksummd5":{"0":"379fb587cd514ec2f9576d728aaa5d50","1":"57934db7336d3de928f125504babe08a","2":"6fbdc7deb426131dda83b689d8372ed8","3":"4c6e11af62414cade90412a292033765"},\
					"checksumsha1":{"0":"8b54cee01a6061f2578bb995ca7e956102399fc5","1":"7a98122912aeedfc09f9843eaad5a29713235d71","2":"e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d","3":"ad1cec36b81a89418bbfde3b0d3c240032d3bfe3"},\
					"bools":{"0":"True","1":"True","2":"False","3":"True"},\
					"hugeints":{"0":"37602","1":"82645","2":"-74956","3":"-80508"}}'.replace("\t","")

	assert pd.DataFrame(col_str).to_json() == expected_json
	assert col_minsizes == {'seq_num': 1, 'float': 3, 'float_neg': 5, 'random': 5, 'dates': 10, 'datetimes': 19, 'texts': 5, 'checksummd5': 32, 'checksumsha1': 40, 'bools': 4, 'hugeints': 5}
	assert col_maxsizes == {'seq_num': 1, 'float': 8, 'float_neg': 9, 'random': 8, 'dates': 10, 'datetimes': 19, 'texts': 20, 'checksummd5': 32, 'checksumsha1': 40, 'bools': 5, 'hugeints': 6}



	data_slice = renderer.slice_data(3, 4, inplace=False)
	result = renderer.calc_column_sizes(data_slice, inplace=False)
	col_str, col_minsizes, col_maxsizes = result

	expected_json = '{"seq_num":{"3":"3","4":"4"},"float":{"3":"1.034483","4":"1.37931"},"float_neg":{"3":"-8.965517","4":"-8.62069"},"random":{"3":"0.349125","4":"0.124884"},"dates":{"3":"2018-01-04","4":"2018-01-05"},"datetimes":{"3":"2018-01-01 03:00:00","4":"2018-01-01 04:00:00"},"texts":{"3":"KkCA4YRzMhctaWAZ5","4":"6B5b0YcBYqcdlkRFo"},"checksummd5":{"3":"4c6e11af62414cade90412a292033765","4":"e6932d483223274bee38f96c2af427be"},"checksumsha1":{"3":"ad1cec36b81a89418bbfde3b0d3c240032d3bfe3","4":"31f9858365b89a683aed53c94839742928eb1028"},"bools":{"3":"True","4":"False"},"hugeints":{"3":"-80508","4":"-78726"}}'.replace("\t","")
	
	assert pd.DataFrame(col_str).to_json() == expected_json
	assert col_minsizes == {'seq_num': 1, 'float': 7, 'float_neg': 8, 'random': 8, 'dates': 10, 'datetimes': 19, 'texts': 17, 'checksummd5': 32, 'checksumsha1': 40, 'bools': 4, 'hugeints': 6}
	assert col_maxsizes == {'seq_num': 1, 'float': 8, 'float_neg': 9, 'random': 8, 'dates': 10, 'datetimes': 19, 'texts': 17, 'checksummd5': 32, 'checksumsha1': 40, 'bools': 5, 'hugeints': 6}
	
	assert len(renderer.col_str.keys()) == 0
	assert len(renderer.col_minsizes.keys()) == 0
	assert len(renderer.col_maxsizes.keys()) == 0
	
def test_calc_columns_offsets():
	renderer = PandasRenderer(data_tiny(), preinit=False)
	data_slice = renderer.slice_data(0, 4, inplace=False)
	r = renderer.calc_column_sizes(data_slice, inplace=False)
	col_str, col_minsizes, col_maxsizes = r

	result = renderer.calc_columns_offsets(col_maxsizes, inplace=False)

	expected = [['seq_num', 0, 1], 
				['float', 3, 8], 
				['float_neg', 13, 9], 
				['random', 24, 8], 
				['dates', 34, 10], 
				['datetimes', 46, 19], 
				['texts', 67, 20], 
				['checksummd5', 89, 32], 
				['checksumsha1', 123, 40], 
				['bools', 165, 5], 
				['hugeints', 172, 6]]

	
	assert all([x[0]==x[1] for x in zip(sum(expected,[]), sum(result, []))])

	result = renderer.calc_columns_offsets(col_minsizes, inplace=False)

	expected = [['seq_num', 0, 1], 
				['float', 3, 3], 
				['float_neg', 8, 5], 
				['random', 15, 5], 
				['dates', 22, 10], 
				['datetimes', 34, 19], 
				['texts', 55, 5], 
				['checksummd5', 62, 32], 
				['checksumsha1', 96, 40], 
				['bools', 138, 4], 
				['hugeints', 144, 5]]


	assert all([x[0]==x[1] for x in zip(sum(expected,[]), sum(result, []))])

	assert len(renderer.col_offsets) == 0

def test_instance():
	renderer = PandasRenderer(data_tiny(), y=0, height=4)

	assert renderer.y == 0
	assert renderer.height == 4

	# make sure we ran the data_slice
	assert renderer.data_slice is not None
	assert renderer.data_slice.shape == (4, 11)
	assert np.all(np.equal(renderer.data_slice.values, data_tiny().values[0:4]))

	# make sure we ran the min/max sizes
	expected_json = '{"seq_num":{"0":"0","1":"1","2":"2","3":"3"},\
					"float":{"0":"0.0","1":"0.344828","2":"0.689655","3":"1.034483"},\
					"float_neg":{"0":"-10.0","1":"-9.655172","2":"-9.310345","3":"-8.965517"},\
					"random":{"0":"0.469527","1":"0.104732","2":"0.975","3":"0.349125"},\
					"dates":{"0":"2018-01-01","1":"2018-01-02","2":"2018-01-03","3":"2018-01-04"},\
					"datetimes":{"0":"2018-01-01 00:00:00","1":"2018-01-01 01:00:00","2":"2018-01-01 02:00:00","3":"2018-01-01 03:00:00"},\
					"texts":{"0":"HY7z5","1":"Bqg3a5HE9bZRS2eXCF5t","2":"PbjBzxilXwxoXGBW1JDz","3":"KkCA4YRzMhctaWAZ5"},\
					"checksummd5":{"0":"379fb587cd514ec2f9576d728aaa5d50","1":"57934db7336d3de928f125504babe08a","2":"6fbdc7deb426131dda83b689d8372ed8","3":"4c6e11af62414cade90412a292033765"},\
					"checksumsha1":{"0":"8b54cee01a6061f2578bb995ca7e956102399fc5","1":"7a98122912aeedfc09f9843eaad5a29713235d71","2":"e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d","3":"ad1cec36b81a89418bbfde3b0d3c240032d3bfe3"},\
					"bools":{"0":"True","1":"True","2":"False","3":"True"},\
					"hugeints":{"0":"37602","1":"82645","2":"-74956","3":"-80508"}}'.replace("\t","")
	

	assert pd.DataFrame(renderer.col_str).to_json() == expected_json
	assert renderer.col_minsizes == {'seq_num': 1, 'float': 3, 'float_neg': 5, 'random': 5, 'dates': 10, 'datetimes': 19, 'texts': 5, 'checksummd5': 32, 'checksumsha1': 40, 'bools': 4, 'hugeints': 5}
	assert renderer.col_maxsizes == {'seq_num': 1, 'float': 8, 'float_neg': 9, 'random': 8, 'dates': 10, 'datetimes': 19, 'texts': 20, 'checksummd5': 32, 'checksumsha1': 40, 'bools': 5, 'hugeints': 6}


	# make sure we ran the offsets
	expected = [['seq_num', 0, 1], 
				['float', 3, 8], 
				['float_neg', 13, 9], 
				['random', 24, 8], 
				['dates', 34, 10], 
				['datetimes', 46, 19], 
				['texts', 67, 20], 
				['checksummd5', 89, 32], 
				['checksumsha1', 123, 40], 
				['bools', 165, 5], 
				['hugeints', 172, 6]]


	
	assert all([x[0]==x[1] for x in zip(sum(expected,[]), sum(renderer.col_offsets, []))])

def test_render():
	renderer = PandasRenderer(data_tiny())
	render_str = renderer.render()
	expected = """0       0.0      -10.0  0.469527  2018-01-01  2018-01-01 00:00:00                 HY7z5  379fb587cd514ec2f9576d728aaa5d50  8b54cee01a6061f2578bb995ca7e956102399fc5   True   37602
				1  0.344828  -9.655172  0.104732  2018-01-02  2018-01-01 01:00:00  Bqg3a5HE9bZRS2eXCF5t  57934db7336d3de928f125504babe08a  7a98122912aeedfc09f9843eaad5a29713235d71   True   82645
				2  0.689655  -9.310345     0.975  2018-01-03  2018-01-01 02:00:00  PbjBzxilXwxoXGBW1JDz  6fbdc7deb426131dda83b689d8372ed8  e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d  False  -74956
				3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00     KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508
				4   1.37931   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00     6B5b0YcBYqcdlkRFo  e6932d483223274bee38f96c2af427be  31f9858365b89a683aed53c94839742928eb1028  False  -78726""".replace("\t","")
	print(render_str)
	assert expected == render_str

	renderer = PandasRenderer(data_tiny(), y=0, height=4)
	render_str = renderer.render()
	expected = """0       0.0      -10.0  0.469527  2018-01-01  2018-01-01 00:00:00                 HY7z5  379fb587cd514ec2f9576d728aaa5d50  8b54cee01a6061f2578bb995ca7e956102399fc5   True   37602
				1  0.344828  -9.655172  0.104732  2018-01-02  2018-01-01 01:00:00  Bqg3a5HE9bZRS2eXCF5t  57934db7336d3de928f125504babe08a  7a98122912aeedfc09f9843eaad5a29713235d71   True   82645
				2  0.689655  -9.310345     0.975  2018-01-03  2018-01-01 02:00:00  PbjBzxilXwxoXGBW1JDz  6fbdc7deb426131dda83b689d8372ed8  e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d  False  -74956
				3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00     KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508""".replace("\t","")
	assert expected == render_str

	renderer = PandasRenderer(data_tiny(), y=0, height=1) # the columns max_sizes differ from the previous example
	render_str = renderer.render()
	expected = """0  0.0  -10.0  0.469527  2018-01-01  2018-01-01 00:00:00  HY7z5  379fb587cd514ec2f9576d728aaa5d50  8b54cee01a6061f2578bb995ca7e956102399fc5  True  37602""".replace("\t","")
	assert expected == render_str


	renderer = PandasRenderer(data_tiny(), y=1, height=3)
	render_str = renderer.render()
	expected = """1  0.344828  -9.655172  0.104732  2018-01-02  2018-01-01 01:00:00  Bqg3a5HE9bZRS2eXCF5t  57934db7336d3de928f125504babe08a  7a98122912aeedfc09f9843eaad5a29713235d71   True   82645
				2  0.689655  -9.310345     0.975  2018-01-03  2018-01-01 02:00:00  PbjBzxilXwxoXGBW1JDz  6fbdc7deb426131dda83b689d8372ed8  e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d  False  -74956
				3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00     KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508""".replace("\t","")
	assert expected == render_str


	renderer = PandasRenderer(data_tiny(), y=1, height=4)
	render_str = renderer.render()
	expected = """1  0.344828  -9.655172  0.104732  2018-01-02  2018-01-01 01:00:00  Bqg3a5HE9bZRS2eXCF5t  57934db7336d3de928f125504babe08a  7a98122912aeedfc09f9843eaad5a29713235d71   True   82645
				2  0.689655  -9.310345     0.975  2018-01-03  2018-01-01 02:00:00  PbjBzxilXwxoXGBW1JDz  6fbdc7deb426131dda83b689d8372ed8  e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d  False  -74956
				3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00     KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508
				4   1.37931   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00     6B5b0YcBYqcdlkRFo  e6932d483223274bee38f96c2af427be  31f9858365b89a683aed53c94839742928eb1028  False  -78726""".replace("\t","")
	assert expected == render_str

	renderer = PandasRenderer(data_tiny(), y=3, height=4)  # the columns max_sizes differ from the previous example
	render_str = renderer.render()
	expected = """3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00  KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508
				4   1.37931   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00  6B5b0YcBYqcdlkRFo  e6932d483223274bee38f96c2af427be  31f9858365b89a683aed53c94839742928eb1028  False  -78726""".replace("\t","")
	assert expected == render_str

	renderer = PandasRenderer(data_tiny(), y=3, height=4, x=0, width=10) 
	render_str = renderer.render()
	expected = """3  1.03448
				4   1.3793""".replace("\t","")
	print(render_str)
	assert expected == render_str


	renderer = PandasRenderer(data_tiny(), y=3, height=4, x=0, width=75) 
	render_str = renderer.render()
	expected = """3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00  KkCA4YRz
				4   1.37931   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00  6B5b0YcB""".replace("\t","")
	print(render_str)
	assert expected == render_str


	renderer = PandasRenderer(data_tiny(), y=3, height=4, x=10, width=65)
	render_str = renderer.render()
	expected = """3  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00  KkCA4YRz
				1   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00  6B5b0YcB""".replace("\t","")
	print(render_str)
	assert expected == render_str

	

def test_render_movement():
	renderer = PandasRenderer(data_tiny())
	render_str = renderer.render()
	expected = """0       0.0      -10.0  0.469527  2018-01-01  2018-01-01 00:00:00                 HY7z5  379fb587cd514ec2f9576d728aaa5d50  8b54cee01a6061f2578bb995ca7e956102399fc5   True   37602
				1  0.344828  -9.655172  0.104732  2018-01-02  2018-01-01 01:00:00  Bqg3a5HE9bZRS2eXCF5t  57934db7336d3de928f125504babe08a  7a98122912aeedfc09f9843eaad5a29713235d71   True   82645
				2  0.689655  -9.310345     0.975  2018-01-03  2018-01-01 02:00:00  PbjBzxilXwxoXGBW1JDz  6fbdc7deb426131dda83b689d8372ed8  e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d  False  -74956
				3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00     KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508
				4   1.37931   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00     6B5b0YcBYqcdlkRFo  e6932d483223274bee38f96c2af427be  31f9858365b89a683aed53c94839742928eb1028  False  -78726""".replace("\t","")
	assert expected == render_str

	#renderer = PandasRenderer(data_tiny(), y=0, height=4)
	render_str = renderer.render(newheight=4)
	expected = """0       0.0      -10.0  0.469527  2018-01-01  2018-01-01 00:00:00                 HY7z5  379fb587cd514ec2f9576d728aaa5d50  8b54cee01a6061f2578bb995ca7e956102399fc5   True   37602
				1  0.344828  -9.655172  0.104732  2018-01-02  2018-01-01 01:00:00  Bqg3a5HE9bZRS2eXCF5t  57934db7336d3de928f125504babe08a  7a98122912aeedfc09f9843eaad5a29713235d71   True   82645
				2  0.689655  -9.310345     0.975  2018-01-03  2018-01-01 02:00:00  PbjBzxilXwxoXGBW1JDz  6fbdc7deb426131dda83b689d8372ed8  e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d  False  -74956
				3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00     KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508""".replace("\t","")
	assert expected == render_str

	#renderer = PandasRenderer(data_tiny(), y=0, height=1) # the columns max_sizes differ from the previous example
	render_str = renderer.render(newheight=1)
	expected = """0  0.0  -10.0  0.469527  2018-01-01  2018-01-01 00:00:00  HY7z5  379fb587cd514ec2f9576d728aaa5d50  8b54cee01a6061f2578bb995ca7e956102399fc5  True  37602""".replace("\t","")
	assert expected == render_str

	#renderer = PandasRenderer(data_tiny(), y=1, height=3)
	render_str = renderer.render(deltay=1, newheight=3)
	expected = """1  0.344828  -9.655172  0.104732  2018-01-02  2018-01-01 01:00:00  Bqg3a5HE9bZRS2eXCF5t  57934db7336d3de928f125504babe08a  7a98122912aeedfc09f9843eaad5a29713235d71   True   82645
				2  0.689655  -9.310345     0.975  2018-01-03  2018-01-01 02:00:00  PbjBzxilXwxoXGBW1JDz  6fbdc7deb426131dda83b689d8372ed8  e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d  False  -74956
				3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00     KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508""".replace("\t","")
	assert expected == render_str

	#renderer = PandasRenderer(data_tiny(), y=1, height=4)
	render_str = renderer.render(newheight=4)
	expected = """1  0.344828  -9.655172  0.104732  2018-01-02  2018-01-01 01:00:00  Bqg3a5HE9bZRS2eXCF5t  57934db7336d3de928f125504babe08a  7a98122912aeedfc09f9843eaad5a29713235d71   True   82645
				2  0.689655  -9.310345     0.975  2018-01-03  2018-01-01 02:00:00  PbjBzxilXwxoXGBW1JDz  6fbdc7deb426131dda83b689d8372ed8  e5b1d5db91d2462cfdf6463a6bb89e34cfb2cb4d  False  -74956
				3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00     KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508
				4   1.37931   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00     6B5b0YcBYqcdlkRFo  e6932d483223274bee38f96c2af427be  31f9858365b89a683aed53c94839742928eb1028  False  -78726""".replace("\t","")
	assert expected == render_str

	#renderer = PandasRenderer(data_tiny(), y=3, height=4)  # the columns max_sizes differ from the previous example
	render_str = renderer.render(deltay=2)
	expected = """3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00  KkCA4YRzMhctaWAZ5  4c6e11af62414cade90412a292033765  ad1cec36b81a89418bbfde3b0d3c240032d3bfe3   True  -80508
				4   1.37931   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00  6B5b0YcBYqcdlkRFo  e6932d483223274bee38f96c2af427be  31f9858365b89a683aed53c94839742928eb1028  False  -78726""".replace("\t","")
	assert expected == render_str

	#renderer = PandasRenderer(data_tiny(), y=3, height=4, x=0, width=10) 
	render_str = renderer.render(newwidth=10)
	expected = """3  1.03448
				4   1.3793""".replace("\t","")
	assert expected == render_str


	#renderer = PandasRenderer(data_tiny(), y=3, height=4, x=0, width=75) 
	render_str = renderer.render(newwidth=75)
	expected = """3  1.034483  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00  KkCA4YRz
				4   1.37931   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00  6B5b0YcB""".replace("\t","")
	assert expected == render_str

	#renderer = PandasRenderer(data_tiny(), y=3, height=4, x=10, width=65)
	render_str = renderer.render(deltax=10, newwidth=65)
	expected = """3  -8.965517  0.349125  2018-01-04  2018-01-01 03:00:00  KkCA4YRz
				1   -8.62069  0.124884  2018-01-05  2018-01-01 04:00:00  6B5b0YcB""".replace("\t","")
	print(render_str)
	assert expected == render_str

	