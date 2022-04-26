(define (crazyTriangle left right depth)

    (define (tree-print depth)
        (define (tree-iter c d i)
            (cond
                ((> i 1) (print " ") (tree-iter c d (- i 1)))
                ((> c d) (print "\n") (tree-iter 0 (+ d 1) (- depth d 1)))
                ((< d depth) (print (get-pascal-num c d) " ") (tree-iter (+ c 1) d i))
            )
        )
        (tree-iter 0 0 depth)
    )
    
    (define (get-pascal-num col depth)
        (cond
            ((= col 0) left)
            ((= col depth) right)
            (else (+ (get-pascal-num (- col 1) (- depth 1)) (get-pascal-num col (- depth 1))))
        )
    )
    
    (tree-print depth)
)

(crazyTriangle 1 1 12)
