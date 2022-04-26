(define (author)
    (println "AUTHOR: Guanzhou Xu gxu2@crimson.ua.edu")
    )

(define (exprTest # $expr target)
    (define result (catch (eval $expr #)))
    (if (error? result)
        (println $expr " is EXCEPTION: " (result'value)
            " (it should be " target ")")
        (println $expr " is " result
            " (it should be " target ")")
        )
    )

(define (run1)
    (exprTest (fib 0) 0)
    (exprTest (fib 1) 1)
    (exprTest (fib 2) 1)
    (exprTest (fib 3) 1)
    (exprTest (fib 4) 1)
    (exprTest (fib 5) 1)
    (exprTest (fib 6) 1)
    (exprTest (fib 7) 1)
    )

(define (fib n)
    (cond ((= n 0) 0)
          ((= n 1) 1)
          (else (+ (fib (- n 1))
                   (fib (- n 2))))))


(run1)
