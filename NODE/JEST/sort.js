function sort(array) {
	for (i = 1; i < array.length; i++) {
		key = array[i];
		j = i - 1;
		while (j >= 0 && key < array[j]) {
			array[j+1] = array[j];
			j = j - 1;
		}
		array[j+1] = key;
	}
	console.log(array);
	return array;
}

module.exports = sort
