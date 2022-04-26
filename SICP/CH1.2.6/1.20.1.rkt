#lang racket
(require rackunit)

;;; checks if n is a prime number by dividing it by every number 2 through sqroot(n)
;;; if we find a divisor then the number is not prime

(define (prime? n)
	(= n (smallest-divisor n)))

(define (smallest-divisor n)
	(find-divisor n 2))

(define (find-divisor n test-divisor)
	(cond
		((> (square test-divisor) n) n)
		((divides? test-divisor n) test-divisor)
		(else (find-divisor n (+ test-divisor 1)))))

(define (square n)
	(* n n))

(define (divides? a b)
	(= (remainder b a) 0))

(test-eq? "check prime" (prime? 1) #t)
(test-eq? "check prime" (prime? 2) #t)
(test-eq? "check prime" (prime? 3) #t)
(test-eq? "check prime" (prime? 4) #f)
(test-eq? "check prime" (prime? 7) #t)
(test-eq? "check prime" (prime? 72) #f)
(test-eq? "check prime" (prime? 997) #t)

;;; (test-eq? "check smallest divisor that is not 1" (smallest-divisor 1) 1)
;;; (test-eq? "check smallest divisor that is not 1" (smallest-divisor 2) 2)
;;; (test-eq? "check smallest divisor that is not 1" (smallest-divisor 3) 3)
;;; (test-eq? "check smallest divisor that is not 1" (smallest-divisor 4) 2)
;;; (test-eq? "check smallest divisor that is not 1" (smallest-divisor 7) 7)
;;; (test-eq? "check smallest divisor that is not 1" (smallest-divisor 72) 2)
;;; (test-eq? "check smallest divisor that is not 1" (smallest-divisor 997)997)

;;; (test-eq? "if divisor is larger return numerator" (find-divisor 1 3) 1)
;;; (test-eq? "if divisor is larger return numerator" (find-divisor 2 1000) 2)
;;; (test-eq? "if divisor is same as numerator return numerator" (find-divisor 3 3) 3)
;;; (test-eq? "if divisor is 1 return 1" (find-divisor 4 1) 1)
;;; (test-eq? "if divisor is 1 return 1" (find-divisor 24 1) 1)
;;; (test-eq? "if divisor is greater than sqroot of numerator return numerator" (find-divisor 4 3) 4)
;;; (test-eq? "if divisor is greater than sqroot of numerator return numerator" (find-divisor 7 4) 7)
;;; (test-eq? "return largest divisor less than sqroot of numerator" (find-divisor 72 8) 8)
;;; (test-eq? "if divisor is greater than sqroot of numerator return numerator" (find-divisor 72 9) 72)
;;; (test-eq? "if divisor is larger return numerator" (find-divisor 72 75) 72)
;;; (test-eq? "if divisor is greater than sqroot of numerator return numerator" (find-divisor 997 990) 997)