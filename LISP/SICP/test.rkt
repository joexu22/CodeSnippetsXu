#lang racket
(>= 2 2)

(let ([x 5]) 5)

(let ([x 5])
	(let ([x 2] [y x])
		(list y x)))