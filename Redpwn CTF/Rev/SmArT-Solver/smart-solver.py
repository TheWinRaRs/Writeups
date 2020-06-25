from z3 import *
tosolve = """(((((((sVar3 < 0x49) || (local_128[1] <= local_128[0])) || (local_128[0] <= local_128[2])) ||
((local_128[3] <= local_128[0] || (local_124 <= local_128[0])))) ||
((((((local_123 <= local_128[0] ||
      ((local_122 <= local_128[0] || (local_128[0] <= local_121)))) ||
     (local_120 <= local_128[0])) ||
    (((((local_11f <= local_128[0] || (local_11e <= local_128[0])) ||
        (local_128[0] <= local_11d)) ||
       (((local_11c <= local_128[0] || (local_128[0] <= local_11b)) ||
         ((local_11a <= local_128[0] ||
           ((local_119 <= local_128[0] || (local_118 <= local_128[0])))))))) ||
      ((local_117 <= local_128[0] ||
        (((local_115 <= local_128[0] || (local_114 <= local_128[0])) ||
          (local_113 <= local_128[0])))))))) ||
   ((((local_112 <= local_128[0] || (local_111 <= local_128[0])) ||
      ((local_110 <= local_128[0] ||
        ((local_128[0] <= local_10f || (local_128[0] <= local_10e)))))) ||
     (local_10d <= local_128[0])))) ||
  (((((((local_10c <= local_128[0] || (local_128[0] <= local_10b)) ||
        (local_10a <= local_128[0])) ||
       ((local_109 <= local_128[0] || (local_108 <= local_128[0])))) ||
      ((local_128[0] <= local_107 ||
        ((local_106 <= local_128[0] || (local_128[0] <= local_105)))))) ||
     (((local_104 <= local_128[0] ||
        (((((local_103 <= local_128[0] || (local_128[0] <= local_102)) ||
            (local_101 <= local_128[0])) ||
           (((local_100 <= local_128[0] || (local_128[0] <= local_ff)) ||
             ((local_fe <= local_128[0] ||
               ((local_128[0] <= local_fd || (local_fc <= local_128[0])))))))) ||
          (local_128[0] <= local_fb)))) ||
       ((((local_128[0] <= local_fa || (local_f9 <= local_128[0])) ||
          (local_f8 <= local_128[0])) ||
         ((local_128[0] <= local_f7 || (local_128[0] <= local_f6)))))))) ||
    (((local_f5 <= local_128[0] || ((local_f4 <= local_128[0] || (local_f3 <= local_128[0]))))
      || (local_f2 <= local_128[0])))))))) ||
((((((((((local_f1 <= local_128[0] || (local_128[0] <= local_f0)) ||
         (local_ef <= local_128[0])) ||
        ((local_ee <= local_128[0] || (local_ed <= local_128[0])))) ||
       (local_ec <= local_128[0])) ||
      (((local_128[0] <= local_eb || (local_ea <= local_128[0])) ||
        ((local_128[0] <= local_e9 ||
          (((local_128[0] <= local_e8 || (local_e7 <= local_128[0])) ||
            (local_128[0] <= local_e6)))))))) ||
     (((local_e5 <= local_128[0] || (local_e4 <= local_128[0])) || (local_e3 <= local_128[0]))
     )) || (((((((local_e2 <= local_128[0] || (local_e1 <= local_128[0])) ||
                 ((local_e0 <= local_128[0] ||
                   (((local_128[1] <= local_128[0] || (local_128[1] <= local_128[2])) ||
                     (local_128[1] <= local_128[3])))))) ||
                ((local_124 <= local_128[1] || (local_123 <= local_128[1])))) ||
               (((local_128[1] <= local_122 ||
                  (((local_128[1] <= local_121 || (local_120 <= local_128[1])) ||
                    ((local_11f <= local_128[1] ||
                      ((((local_128[1] <= local_11e || (local_128[1] <= local_11d)) ||
                         (local_128[1] <= local_11c)) ||
                        ((local_128[1] <= local_11b || (local_11a <= local_128[1])))))))))) ||
                 ((local_119 <= local_128[1] ||
                   ((local_118 <= local_128[1] || (local_117 <= local_128[1])))))))) ||
              ((((local_128[1] <= local_116 ||
                  (((local_115 <= local_128[1] || (local_114 <= local_128[1])) ||
                    (local_128[1] <= local_113)))) ||
                 ((((local_112 <= local_128[1] || (local_111 <= local_128[1])) ||
                    (local_110 <= local_128[1])) ||
                   ((local_128[1] <= local_10f || (local_128[1] <= local_10e)))))) ||
                (((((((local_10d <= local_128[1] ||
                       (((local_10c <= local_128[1] || (local_128[1] <= local_10b)) ||
                         (local_10a <= local_128[1])))) ||
                      (((local_109 <= local_128[1] || (local_128[1] <= local_108)) ||
                        ((local_128[1] <= local_107 ||
                          ((((local_128[1] <= local_105 || (local_104 <= local_128[1])) ||
                             ((local_103 <= local_128[1] ||
                               ((((local_128[1] <= local_102 || (local_101 <= local_128[1])) ||
                                  (local_128[1] <= local_100)) ||
                                 ((local_128[1] <= local_ff || (local_fe <= local_128[1])))))))) ||
                            (local_128[1] <= local_fd)))))))) ||
                     (((local_128[1] <= local_fb || (local_128[1] <= local_fa)) ||
                       ((((local_f9 <= local_128[1] ||
                           (((local_f8 <= local_128[1] || (local_128[1] <= local_f7)) ||
                             (local_128[1] <= local_f6)))) ||
                          (((local_128[1] <= local_f5 || (local_f4 <= local_128[1])) ||
                            (local_f3 <= local_128[1])))) ||
                         ((local_f2 <= local_128[1] || (local_f1 <= local_128[1])))))))) ||
                    ((local_128[1] <= local_f0 ||
                      (((local_ef <= local_128[1] || (local_ee <= local_128[1])) ||
                        (local_ed <= local_128[1])))))) ||
                   (((((local_ec <= local_128[1] || (local_128[1] <= local_eb)) ||
                       (local_ea <= local_128[1])) ||
                      (((local_128[1] <= local_e9 || (local_128[1] <= local_e8)) ||
                        ((local_e7 <= local_128[1] ||
                          ((((((local_128[1] <= local_e6 || (local_e4 <= local_128[1])) ||
                               (local_e3 <= local_128[1])) ||
                              ((local_128[1] <= local_e2 || (local_e1 <= local_128[1])))) ||
                             (local_e0 <= local_128[1])) ||
                            ((local_128[0] <= local_128[2] || (local_128[1] <= local_128[2]))))))))))
                     || ((((local_128[3] <= local_128[2] ||
                            ((((local_124 <= local_128[2] || (local_123 <= local_128[2])) ||
                               (local_122 <= local_128[2])) ||
                              ((local_121 <= local_128[2] || (local_120 <= local_128[2])))))) ||
                           ((((local_11f <= local_128[2] ||
                               ((local_11e <= local_128[2] || (local_11d <= local_128[2])))) ||
                              (local_11c <= local_128[2])) ||
                             (((local_11b <= local_128[2] || (local_11a <= local_128[2])) ||
                               (local_119 <= local_128[2])))))) ||
                          ((((local_118 <= local_128[2] || (local_117 <= local_128[2])) ||
                             ((local_116 <= local_128[2] ||
                               ((local_115 <= local_128[2] || (local_114 <= local_128[2])))))) ||
                            (local_113 <= local_128[2])))))))) ||
                  (((((local_112 <= local_128[2] || (local_111 <= local_128[2])) ||
                      (local_110 <= local_128[2])) ||
                     ((local_10f <= local_128[2] || (local_10e <= local_128[2])))) ||
                    ((local_10d <= local_128[2] ||
                      ((local_10c <= local_128[2] || (local_10b <= local_128[2])))))))))))) ||
             ((local_10a <= local_128[2] ||
               (((local_109 <= local_128[2] || (local_108 <= local_128[2])) ||
                 (local_107 <= local_128[2])))))))) ||
   (((((local_106 <= local_128[2] || (local_104 <= local_128[2])) ||
       ((((((((((local_103 <= local_128[2] ||
                 ((local_102 <= local_128[2] || (local_101 <= local_128[2])))) ||
                (local_100 <= local_128[2])) ||
               ((((local_fe <= local_128[2] || (local_fd <= local_128[2])) ||
                  (local_fc <= local_128[2])) ||
                 (((local_fb <= local_128[2] || (local_f9 <= local_128[2])) ||
                   ((local_f8 <= local_128[2] ||
                     ((local_f7 <= local_128[2] || (local_f6 <= local_128[2])))))))))) ||
              ((((local_f5 <= local_128[2] ||
                  ((((local_f4 <= local_128[2] || (local_f3 <= local_128[2])) ||
                     (local_f2 <= local_128[2])) ||
                    ((local_f1 <= local_128[2] || (local_ef <= local_128[2])))))) ||
                 ((local_ee <= local_128[2] ||
                   ((local_ed <= local_128[2] || (local_ec <= local_128[2])))))) ||
                (local_ea <= local_128[2])))) ||
             (((local_e9 <= local_128[2] || (local_e7 <= local_128[2])) ||
               (local_e5 <= local_128[2])))) ||
            ((((local_e4 <= local_128[2] || (local_e3 <= local_128[2])) ||
               (((local_e2 <= local_128[2] ||
                  ((local_e1 <= local_128[2] || (local_e0 <= local_128[2])))) ||
                 (local_128[3] <= local_128[0])))) ||
              (((((((((local_128[1] <= local_128[3] || (local_128[3] <= local_128[2])) ||
                      (local_124 <= local_128[3])) ||
                     (((local_123 <= local_128[3] || (local_122 <= local_128[3])) ||
                       ((local_128[3] <= local_121 ||
                         ((local_120 <= local_128[3] || (local_11f <= local_128[3])))))))) ||
                    (local_11e <= local_128[3])) ||
                   (((((local_128[3] <= local_11d || (local_11c <= local_128[3])) ||
                       (local_128[3] <= local_11b)) ||
                      ((local_11a <= local_128[3] || (local_119 <= local_128[3])))) ||
                     (local_118 <= local_128[3])))) ||
                  ((local_117 <= local_128[3] || (local_128[3] <= local_116)))) ||
                 ((local_115 <= local_128[3] ||
                   (((local_114 <= local_128[3] || (local_113 <= local_128[3])) ||
                     (local_112 <= local_128[3])))))) ||
                (((((local_111 <= local_128[3] || (local_110 <= local_128[3])) ||
                    (local_128[3] <= local_10f)) ||
                   ((local_128[3] <= local_10e || (local_10d <= local_128[3])))) ||
                  ((local_10c <= local_128[3] ||
                    (((local_128[3] <= local_10b || (local_10a <= local_128[3])) ||
                      (local_109 <= local_128[3])))))))))))) ||
           (((local_108 <= local_128[3] || (local_128[3] <= local_107)) ||
             ((local_106 <= local_128[3] ||
               (((local_128[3] <= local_105 || (local_104 <= local_128[3])) ||
                 ((local_103 <= local_128[3] ||
                   ((((local_128[3] <= local_102 || (local_101 <= local_128[3])) ||
                      (local_128[3] <= local_ff)) ||
                     ((local_fe <= local_128[3] || (local_128[3] <= local_fd)))))))))))))) ||
          ((local_fc <= local_128[3] ||
            ((local_128[3] <= local_fb || (local_128[3] <= local_fa)))))) ||
         (((((local_f9 <= local_128[3] ||
              (((local_f8 <= local_128[3] || (local_128[3] <= local_f7)) ||
                (local_128[3] <= local_f6)))) ||
             (((local_f5 <= local_128[3] || (local_f4 <= local_128[3])) ||
               (local_f3 <= local_128[3])))) ||
            ((local_f2 <= local_128[3] || (local_f1 <= local_128[3])))) ||
           ((local_128[3] <= local_f0 ||
             (((local_ef <= local_128[3] || (local_ee <= local_128[3])) ||
               (local_ed <= local_128[3])))))))))) ||
      (((((((local_ec <= local_128[3] || (local_128[3] <= local_eb)) ||
            ((local_ea <= local_128[3] ||
              (((local_128[3] <= local_e9 || (local_128[3] <= local_e8)) ||
                ((local_e7 <= local_128[3] ||
                  ((((local_128[3] <= local_e6 || (local_e5 <= local_128[3])) ||
                     (local_e4 <= local_128[3])) ||
                    ((local_e3 <= local_128[3] || (local_e2 <= local_128[3])))))))))))) ||
           (local_e1 <= local_128[3])) ||
          ((local_e0 <= local_128[3] || (local_124 <= local_128[0])))) ||
         ((((((local_124 <= local_128[1] ||
               (((local_124 <= local_128[2] || (local_124 <= local_128[3])) ||
                 (local_124 <= local_123)))) ||
              (((local_124 <= local_122 || (local_124 <= local_121)) || (local_124 <= local_120))
              )) || (((local_124 <= local_11f || (local_124 <= local_11e)) ||
                      ((local_124 <= local_11d ||
                        (((local_124 <= local_11c || (local_124 <= local_11b)) ||
                          (local_124 <= local_11a)))))))) ||
            ((local_124 <= local_119 || (local_124 <= local_118)))) ||
           (((local_124 <= local_117 ||
              ((((local_124 <= local_116 || (local_124 <= local_115)) ||
                 ((local_124 <= local_114 ||
                   (((((local_124 <= local_113 || (local_124 <= local_112)) ||
                       (local_124 <= local_111)) ||
                      ((local_124 <= local_110 || (local_124 <= local_10f)))) ||
                     (local_124 <= local_10e)))))) ||
                ((local_124 <= local_10d || (local_124 <= local_10c)))))) ||
             (local_124 <= local_10b)))))) ||
        (((((((local_124 <= local_10a || (local_124 <= local_109)) || (local_124 <= local_108))
             || (((local_124 <= local_107 || (local_124 <= local_106)) ||
                  ((local_124 <= local_105 ||
                    ((local_124 <= local_104 || (local_124 <= local_103)))))))) ||
            ((local_124 <= local_102 ||
              ((((local_124 <= local_101 || (local_124 <= local_100)) || (local_124 <= local_ff))
                || ((local_124 <= local_fe || (local_124 <= local_fd)))))))) ||
           (((((local_124 <= local_fc || ((local_124 <= local_fb || (local_124 <= local_fa)))) ||
               (local_124 <= local_f9)) ||
              ((((((local_124 <= local_f8 || (local_124 <= local_f7)) || (local_124 <= local_f6))
                  || ((local_124 <= local_f5 || (local_124 <= local_f4)))) ||
                 ((local_124 <= local_f3 || ((local_124 <= local_f2 || (local_124 <= local_f1))))))
                || (local_124 <= local_f0)))) ||
             (((local_124 <= local_ef || (local_124 <= local_ee)) || (local_124 <= local_ed))))))
          || (((((local_124 <= local_ec || (local_124 <= local_eb)) ||
                 ((local_124 <= local_ea || ((local_124 <= local_e9 || (local_124 <= local_e8)))))
                 ) || ((local_124 <= local_e7 ||
                        (((local_124 <= local_e6 || (local_124 <= local_e5)) ||
                          (local_124 <= local_e4)))))) ||
               (((local_124 <= local_e3 || (local_124 <= local_e2)) ||
                 ((local_124 <= local_e1 ||
                   ((local_e0 <= local_124 || (local_123 <= local_128[0])))))))))))))) ||
     (((((local_123 <= local_128[1] ||
          ((((local_123 <= local_128[2] || (local_123 <= local_128[3])) ||
             (local_124 <= local_123)) || ((local_123 <= local_122 || (local_123 <= local_121))))
          )) || (((local_123 <= local_120 ||
                   ((local_11f <= local_123 || (local_123 <= local_11e)))) ||
                  ((local_123 <= local_11d ||
                    ((((local_123 <= local_11c || (local_123 <= local_11b)) ||
                       (local_123 <= local_11a)) ||
                      (((local_123 <= local_119 || (local_118 <= local_123)) ||
                        ((local_123 <= local_117 ||
                          ((local_123 <= local_116 || (local_123 <= local_115)))))))))))))) ||
        (((local_114 <= local_123 ||
           ((((((local_123 <= local_113 || (local_112 <= local_123)) || (local_123 <= local_111))
               || ((local_123 <= local_110 || (local_123 <= local_10f)))) ||
              ((((((local_123 <= local_10e ||
                    ((local_123 <= local_10d || (local_10c <= local_123)))) ||
                   (local_123 <= local_10b)) ||
                  ((((((local_123 <= local_10a || (local_123 <= local_108)) ||
                       (local_123 <= local_107)) ||
                      ((local_123 <= local_106 || (local_123 <= local_105)))) ||
                     (local_104 <= local_123)) ||
                    ((local_103 <= local_123 || (local_123 <= local_102)))))) ||
                 ((local_123 <= local_101 ||
                   (((local_123 <= local_100 || (local_123 <= local_ff)) || (local_123 <= local_fe))
                   )))) || ((((local_123 <= local_fd || (local_123 <= local_fc)) ||
                              (local_123 <= local_fb)) ||
                             ((local_123 <= local_fa || (local_123 <= local_f9)))))))) ||
             ((local_123 <= local_f8 ||
               (((local_123 <= local_f7 || (local_123 <= local_f6)) || (local_123 <= local_f5))))))
           )) || (((((((local_123 <= local_f4 || (local_f3 <= local_123)) ||
                       ((local_123 <= local_f1 ||
                         (((local_123 <= local_f0 || (local_ef <= local_123)) ||
                           ((local_123 <= local_ed ||
                             ((((local_123 <= local_ec || (local_123 <= local_eb)) ||
                                (local_123 <= local_e9)) ||
                               ((local_123 <= local_e8 || (local_123 <= local_e7)))))))))))) ||
                      (local_123 <= local_e6)) ||
                     (((local_123 <= local_e5 || (local_e4 <= local_123)) ||
                       (((local_123 <= local_e3 ||
                          (((local_123 <= local_e2 || (local_123 <= local_e1)) ||
                            (local_e0 <= local_123)))) ||
                         (((local_122 <= local_128[0] || (local_128[1] <= local_122)) ||
                           (local_122 <= local_128[2])))))))) ||
                    (((local_122 <= local_128[3] || (local_124 <= local_122)) ||
                      ((local_123 <= local_122 ||
                        (((local_122 <= local_121 || (local_120 <= local_122)) ||
                          (local_11f <= local_122)))))))) ||
                   ((local_11e <= local_122 || (local_122 <= local_11d)))))))) ||
       ((((local_11c <= local_122 ||
           (((local_122 <= local_11b || (local_11a <= local_122)) ||
             ((local_119 <= local_122 ||
               ((((local_118 <= local_122 || (local_117 <= local_122)) || (local_122 <= local_116))
                 || ((local_115 <= local_122 || (local_114 <= local_122)))))))))) ||
          (local_113 <= local_122)) ||
         (((((((local_112 <= local_122 || (local_111 <= local_122)) ||
               (((local_110 <= local_122 ||
                  (((local_122 <= local_10f || (local_122 <= local_10e)) ||
                    (local_10d <= local_122)))) ||
                 (((local_10c <= local_122 || (local_122 <= local_10b)) || (local_10a <= local_122)
                   ))))) ||
              (((local_109 <= local_122 || (local_122 <= local_107)) ||
                (((local_106 <= local_122 ||
                   (((local_122 <= local_105 || (local_104 <= local_122)) ||
                     (local_103 <= local_122)))) ||
                  (((local_122 <= local_102 || (local_101 <= local_122)) ||
                    ((local_122 <= local_100 ||
                      (((((((local_122 <= local_ff || (local_fe <= local_122)) ||
                            ((local_122 <= local_fd ||
                              (((((local_fc <= local_122 || (local_122 <= local_fb)) ||
                                  (local_122 <= local_fa)) ||
                                 ((local_f9 <= local_122 || (local_f8 <= local_122)))) ||
                                (local_122 <= local_f7)))))) ||
                           ((local_122 <= local_f6 || (local_f4 <= local_122)))) ||
                          (local_f3 <= local_122)) ||
                         (((((local_f2 <= local_122 || (local_f1 <= local_122)) ||
                             (local_122 <= local_f0)) ||
                            (((local_ef <= local_122 || (local_ee <= local_122)) ||
                              ((local_ed <= local_122 ||
                                ((local_ec <= local_122 || (local_122 <= local_eb)))))))) ||
                           (local_ea <= local_122)))) ||
                        (((local_122 <= local_e9 || (local_122 <= local_e8)) || (local_e7 <= local_122)
                          ))))))))))))) ||
             (((local_122 <= local_e6 || (local_e5 <= local_122)) ||
               (((((local_e4 <= local_122 || ((local_e3 <= local_122 || (local_e2 <= local_122))))
                   || (local_e1 <= local_122)) ||
                  ((((((local_e0 <= local_122 || (local_128[0] <= local_121)) ||
                       (local_128[1] <= local_121)) ||
                      ((local_121 <= local_128[2] || (local_128[3] <= local_121)))) ||
                     ((local_124 <= local_121 ||
                       ((local_123 <= local_121 || (local_122 <= local_121)))))) ||
                    (local_120 <= local_121)))) ||
                 (((((local_11f <= local_121 || (local_11e <= local_121)) ||
                     (local_121 <= local_11d)) ||
                    (((local_11c <= local_121 || (local_121 <= local_11b)) ||
                      ((local_11a <= local_121 ||
                        ((local_119 <= local_121 || (local_118 <= local_121)))))))) ||
                   (local_117 <= local_121)))))))) ||
            ((((((local_116 <= local_121 || (local_115 <= local_121)) || (local_114 <= local_121))
                || ((((local_113 <= local_121 || (local_112 <= local_121)) ||
                      ((local_111 <= local_121 ||
                        ((local_110 <= local_121 || (local_121 <= local_10e)))))) ||
                     ((local_10d <= local_121 ||
                       ((((local_10c <= local_121 || (local_10a <= local_121)) ||
                          (local_109 <= local_121)) ||
                         ((local_108 <= local_121 || (local_106 <= local_121)))))))))) ||
               (((local_121 <= local_105 || ((local_104 <= local_121 || (local_103 <= local_121))))
                 || ((local_121 <= local_102 ||
                      ((((local_101 <= local_121 || (local_100 <= local_121)) ||
                         (local_121 <= local_ff)) ||
                        (((local_fe <= local_121 || (local_121 <= local_fd)) ||
                          ((local_fc <= local_121 ||
                            ((local_121 <= local_fa || (local_f9 <= local_121)))))))))))))) ||
              ((local_f8 <= local_121 ||
                (((local_121 <= local_f6 || (local_f5 <= local_121)) || (local_f4 <= local_121))))))
            )) || ((((local_f3 <= local_121 || (local_f2 <= local_121)) ||
                     ((((((((local_f1 <= local_121 ||
                             ((local_121 <= local_f0 || (local_ef <= local_121)))) ||
                            (local_ee <= local_121)) ||
                           ((((((local_ed <= local_121 || (local_ec <= local_121)) ||
                                (local_121 <= local_eb)) ||
                               ((local_ea <= local_121 || (local_121 <= local_e8)))) ||
                              (local_e7 <= local_121)) ||
                             (((local_121 <= local_e6 || (local_e5 <= local_121)) ||
                               ((local_e4 <= local_121 ||
                                 (((local_e3 <= local_121 || (local_e2 <= local_121)) ||
                                   (local_e1 <= local_121)))))))))) ||
                          (((local_e0 <= local_121 || (local_120 <= local_128[0])) ||
                            (local_120 <= local_128[1])))) ||
                         (((local_120 <= local_128[2] || (local_120 <= local_128[3])) ||
                           ((local_124 <= local_120 ||
                             (((local_123 <= local_120 || (local_120 <= local_122)) ||
                               (local_120 <= local_121)))))))) ||
                        ((local_11f <= local_120 || (local_120 <= local_11e)))) ||
                       (((local_120 <= local_11d ||
                          (((local_120 <= local_11c || (local_120 <= local_11b)) ||
                            ((local_11a <= local_120 ||
                              ((((local_120 <= local_119 || (local_118 <= local_120)) ||
                                 (local_120 <= local_117)) ||
                                ((local_120 <= local_116 || (local_120 <= local_115)))))))))) ||
                         (local_114 <= local_120)))))) ||
                    ((local_120 <= local_113 || (local_112 <= local_120)))))))))))))) ||
(((((((local_120 <= local_111 ||
       (((local_120 <= local_110 || (local_120 <= local_10f)) || (local_120 <= local_10e))))
      || ((((local_120 <= local_10d || (local_10c <= local_120)) || (local_120 <= local_10b))
           || ((local_10a <= local_120 || (local_109 <= local_120)))))) ||
     ((local_120 <= local_108 ||
       (((local_120 <= local_107 || (local_120 <= local_106)) || (local_120 <= local_105))))))
    || ((((local_104 <= local_120 || (local_103 <= local_120)) ||
          ((local_120 <= local_102 ||
            (((local_120 <= local_101 || (local_120 <= local_100)) ||
              ((local_120 <= local_ff ||
                ((((local_120 <= local_fe || (local_120 <= local_fd)) || (local_120 <= local_fc))
                  || ((local_120 <= local_fb || (local_120 <= local_fa)))))))))))) ||
         (local_f9 <= local_120)))) ||
   ((((local_120 <= local_f8 || (local_120 <= local_f7)) ||
      ((((local_120 <= local_f6 ||
          (((local_120 <= local_f5 || (local_120 <= local_f4)) || (local_f3 <= local_120)))) ||
         (((local_f2 <= local_120 || (local_120 <= local_f1)) || (local_120 <= local_f0)))) ||
        ((local_ef <= local_120 || (local_ee <= local_120)))))) ||
     ((((local_120 <= local_ed ||
         (((local_120 <= local_ec || (local_120 <= local_eb)) || (local_ea <= local_120)))) ||
        (((local_120 <= local_e9 || (local_120 <= local_e8)) ||
          ((local_120 <= local_e7 ||
            (((local_120 <= local_e6 || (local_120 <= local_e5)) ||
              ((local_e4 <= local_120 ||
                (((((((local_e3 <= local_120 || (local_120 <= local_e2)) || (local_e1 <= local_120)
                      ) || ((local_e0 <= local_120 || (local_11f <= local_128[0])))) ||
                    (local_11f <= local_128[1])) ||
                   ((local_11f <= local_128[2] || (local_11f <= local_128[3])))) ||
                  (local_124 <= local_11f)))))))))))) ||
       (((((local_11f <= local_123 || (local_11f <= local_122)) || (local_11f <= local_121)) ||
          ((local_11f <= local_120 || (local_11f <= local_11e)))) || (local_11f <= local_11d))))
     )))) || (((((((local_11f <= local_11c || (local_11f <= local_11b)) ||
                   ((local_11f <= local_11a ||
                     (((local_11f <= local_119 || (local_118 <= local_11f)) ||
                       (local_11f <= local_117)))))) ||
                  ((local_11f <= local_116 || (local_11f <= local_115)))) ||
                 (local_114 <= local_11f)) ||
                ((((local_11f <= local_113 || (local_11f <= local_111)) ||
                   ((local_11f <= local_110 ||
                     ((((local_11f <= local_10f || (local_11f <= local_10e)) ||
                        (local_11f <= local_10d)) ||
                       ((local_10c <= local_11f || (local_11f <= local_10b)))))))) ||
                  ((local_11f <= local_10a ||
                    ((local_11f <= local_109 || (local_11f <= local_108)))))))) ||
               (((((local_11f <= local_107 ||
                    (((local_11f <= local_106 || (local_11f <= local_105)) ||
                      (local_104 <= local_11f)))) ||
                   (((local_103 <= local_11f || (local_11f <= local_102)) ||
                     (local_11f <= local_101)))) ||
                  (((local_11f <= local_100 || (local_11f <= local_ff)) ||
                    ((local_11f <= local_fe ||
                      (((local_11f <= local_fd || (local_11f <= local_fc)) ||
                        (local_11f <= local_fb)))))))) ||
                 ((((((local_11f <= local_fa || (local_11f <= local_f9)) ||
                      (local_11f <= local_f8)) ||
                     (((local_11f <= local_f7 || (local_11f <= local_f6)) ||
                       ((local_11f <= local_f5 ||
                         ((((local_11f <= local_f4 || (local_f3 <= local_11f)) ||
                            (local_11f <= local_f2)) ||
                           ((local_11f <= local_f1 || (local_11f <= local_f0)))))))))) ||
                    ((local_11f <= local_ee ||
                      ((local_11f <= local_ed || (local_11f <= local_ec)))))) ||
                   ((((local_11f <= local_eb ||
                       (((local_11f <= local_ea || (local_11f <= local_e9)) ||
                         (local_11f <= local_e8)))) ||
                      (((local_11f <= local_e7 || (local_11f <= local_e6)) ||
                        (local_11f <= local_e5)))) ||
                     (((local_e4 <= local_11f || (local_11f <= local_e3)) ||
                       (((local_11f <= local_e2 ||
                          (((local_11f <= local_e1 || (local_e0 <= local_11f)) ||
                            (local_11e <= local_128[0])))) ||
                         ((local_128[1] <= local_11e || (local_11e <= local_128[2]))))))))))))))))))
)) || ((((((((local_11e <= local_128[3] ||
              ((((((local_124 <= local_11e || (local_123 <= local_11e)) ||
                   ((local_11e <= local_122 ||
                     (((((local_11e <= local_121 || (local_120 <= local_11e)) ||
                         (local_11f <= local_11e)) ||
                        ((local_11e <= local_11d || (local_11c <= local_11e)))) ||
                       (local_11e <= local_11b)))))) ||
                  ((local_11a <= local_11e || (local_119 <= local_11e)))) ||
                 (local_118 <= local_11e)) ||
                (((local_117 <= local_11e || (local_11e <= local_116)) ||
                  (local_115 <= local_11e)))))) ||
             ((((local_114 <= local_11e || (local_113 <= local_11e)) ||
                ((local_112 <= local_11e ||
                  ((local_111 <= local_11e || (local_110 <= local_11e)))))) ||
               ((local_11e <= local_10f ||
                 (((local_11e <= local_10e || (local_10d <= local_11e)) ||
                   (local_10c <= local_11e)))))))) ||
            (((((local_11e <= local_10b || (local_10a <= local_11e)) ||
                (((((local_109 <= local_11e ||
                     ((local_11e <= local_108 || (local_11e <= local_107)))) ||
                    (local_106 <= local_11e)) ||
                   (((((local_11e <= local_105 || (local_104 <= local_11e)) ||
                       (local_103 <= local_11e)) ||
                      ((local_11e <= local_102 || (local_101 <= local_11e)))) ||
                     ((local_11e <= local_100 ||
                       ((local_11e <= local_ff || (local_fe <= local_11e)))))))) ||
                  (local_11e <= local_fd)))) ||
               (((((local_fc <= local_11e || (local_11e <= local_fb)) ||
                   (local_11e <= local_fa)) ||
                  (((local_f9 <= local_11e || (local_f8 <= local_11e)) ||
                    ((local_11e <= local_f7 ||
                      ((local_11e <= local_f6 || (local_11e <= local_f5)))))))) ||
                 (local_f4 <= local_11e)))) ||
              ((((local_f3 <= local_11e || (local_f2 <= local_11e)) || (local_f1 <= local_11e))
                || ((local_11e <= local_f0 || (local_ef <= local_11e)))))))) ||
           ((((((((((((local_ee <= local_11e ||
                       ((local_ed <= local_11e || (local_ec <= local_11e)))) ||
                      ((local_11e <= local_eb ||
                        ((((local_ea <= local_11e || (local_11e <= local_e9)) ||
                           (local_11e <= local_e8)) ||
                          ((local_e7 <= local_11e || (local_11e <= local_e6)))))))) ||
                     ((local_e5 <= local_11e ||
                       ((local_e4 <= local_11e || (local_e3 <= local_11e)))))) ||
                    ((local_e1 <= local_11e ||
                      (((((local_e0 <= local_11e || (local_128[0] <= local_11d)) ||
                          (local_128[1] <= local_11d)) ||
                         (((local_11d <= local_128[2] || (local_128[3] <= local_11d)) ||
                           ((local_124 <= local_11d ||
                             ((local_123 <= local_11d || (local_122 <= local_11d)))))))) ||
                        ((local_121 <= local_11d ||
                          (((local_120 <= local_11d || (local_11f <= local_11d)) ||
                            (local_11e <= local_11d)))))))))) ||
                   (((local_11c <= local_11d || (local_11d <= local_11b)) ||
                     (((local_11a <= local_11d ||
                        ((local_119 <= local_11d || (local_118 <= local_11d)))) ||
                       (local_117 <= local_11d)))))) ||
                  ((((((local_116 <= local_11d || (local_115 <= local_11d)) ||
                       (local_114 <= local_11d)) ||
                      ((local_113 <= local_11d || (local_112 <= local_11d)))) ||
                     (local_111 <= local_11d)) ||
                    (((local_110 <= local_11d || (local_10f <= local_11d)) ||
                      ((local_10e <= local_11d ||
                        (((local_10d <= local_11d || (local_10c <= local_11d)) ||
                          (local_10b <= local_11d)))))))))) ||
                 ((local_10a <= local_11d || (local_109 <= local_11d)))) ||
                ((local_108 <= local_11d ||
                  (((((local_107 <= local_11d || (local_106 <= local_11d)) ||
                      ((local_11d <= local_105 ||
                        (((local_104 <= local_11d || (local_103 <= local_11d)) ||
                          (local_102 <= local_11d)))))) ||
                     ((local_101 <= local_11d || (local_100 <= local_11d)))) ||
                    (((((local_11d <= local_ff ||
                         (((local_fe <= local_11d || (local_fd <= local_11d)) ||
                           ((local_fc <= local_11d ||
                             ((((local_fb <= local_11d || (local_11d <= local_fa)) ||
                                (local_f9 <= local_11d)) ||
                               ((local_f8 <= local_11d || (local_f7 <= local_11d)))))))))) ||
                        (local_f6 <= local_11d)) ||
                       ((((local_f5 <= local_11d || (local_f4 <= local_11d)) ||
                          ((local_f3 <= local_11d ||
                            (((local_f2 <= local_11d || (local_f1 <= local_11d)) ||
                              (local_11d <= local_f0)))))) ||
                         ((((local_ef <= local_11d || (local_ee <= local_11d)) ||
                            (local_ed <= local_11d)) ||
                           ((local_ec <= local_11d || (local_11d <= local_eb)))))))) ||
                      (((((local_ea <= local_11d ||
                           (((local_e9 <= local_11d || (local_11d <= local_e8)) ||
                             (local_e7 <= local_11d)))) ||
                          (((local_11d <= local_e6 || (local_e5 <= local_11d)) ||
                            ((local_e4 <= local_11d ||
                              ((((local_e3 <= local_11d || (local_e2 <= local_11d)) ||
                                 ((local_e1 <= local_11d ||
                                   ((((local_e0 <= local_11d || (local_11c <= local_128[0])) ||
                                      (local_128[1] <= local_11c)) ||
                                     ((local_11c <= local_128[2] || (local_11c <= local_128[3]))))))))
                                || (local_124 <= local_11c)))))))) ||
                         ((local_123 <= local_11c || (local_11c <= local_122)))) ||
                        ((((local_11c <= local_121 ||
                            (((local_120 <= local_11c || (local_11f <= local_11c)) ||
                              (local_11c <= local_11e)))) ||
                           (((local_11c <= local_11d || (local_11c <= local_11b)) ||
                             (local_11a <= local_11c)))) ||
                          (((local_119 <= local_11c || (local_118 <= local_11c)) ||
                            ((local_117 <= local_11c ||
                              (((local_11c <= local_116 || (local_115 <= local_11c)) ||
                                (local_114 <= local_11c)))))))))))))))))) ||
               (((((local_11c <= local_113 || (local_112 <= local_11c)) ||
                   ((local_111 <= local_11c ||
                     (((local_110 <= local_11c || (local_11c <= local_10f)) ||
                       ((local_11c <= local_10e ||
                         ((((((local_10d <= local_11c || (local_10c <= local_11c)) ||
                              (local_11c <= local_10b)) ||
                             ((local_10a <= local_11c || (local_109 <= local_11c)))) ||
                            (local_11c <= local_108)) ||
                           ((local_11c <= local_107 || (local_106 <= local_11c)))))))))))) ||
                  (((local_11c <= local_105 ||
                     ((((((local_104 <= local_11c || (local_103 <= local_11c)) ||
                          (local_11c <= local_102)) ||
                         ((local_101 <= local_11c || (local_11c <= local_100)))) ||
                        (((local_11c <= local_ff ||
                           ((local_fe <= local_11c || (local_11c <= local_fd)))) ||
                          (local_fc <= local_11c)))) ||
                       (((local_11c <= local_fb || (local_11c <= local_fa)) ||
                         (local_f9 <= local_11c)))))) ||
                    (((local_f8 <= local_11c || (local_11c <= local_f7)) ||
                      ((local_11c <= local_f6 ||
                        ((local_11c <= local_f5 || (local_f4 <= local_11c)))))))))) ||
                 (local_f3 <= local_11c)))) ||
              (((((((((local_f2 <= local_11c || (local_f1 <= local_11c)) ||
                      (local_11c <= local_f0)) ||
                     ((local_ef <= local_11c || (local_ee <= local_11c)))) ||
                    ((local_ed <= local_11c ||
                      ((local_ec <= local_11c || (local_11c <= local_eb)))))) ||
                   ((local_ea <= local_11c ||
                     (((local_11c <= local_e9 || (local_11c <= local_e8)) ||
                       (local_e7 <= local_11c)))))) ||
                  ((((local_11c <= local_e6 || (local_e5 <= local_11c)) ||
                     ((local_e4 <= local_11c ||
                       ((local_e3 <= local_11c || (local_11c <= local_e2)))))) ||
                    ((local_e1 <= local_11c ||
                      ((((local_e0 <= local_11c || (local_128[0] <= local_11b)) ||
                         (local_128[1] <= local_11b)) ||
                        (((local_11b <= local_128[2] || (local_128[3] <= local_11b)) ||
                          ((local_124 <= local_11b ||
                            ((local_123 <= local_11b || (local_122 <= local_11b)))))))))))))) ||
                 (((((local_121 <= local_11b ||
                      ((((local_120 <= local_11b || (local_11f <= local_11b)) ||
                         (local_11e <= local_11b)) ||
                        ((local_11d <= local_11b || (local_11c <= local_11b)))))) ||
                     ((local_11a <= local_11b ||
                       ((local_119 <= local_11b || (local_118 <= local_11b)))))) ||
                    (local_117 <= local_11b)) ||
                   (((local_116 <= local_11b || (local_115 <= local_11b)) ||
                     (local_114 <= local_11b)))))) ||
                (((local_113 <= local_11b || (local_112 <= local_11b)) ||
                  ((((((local_111 <= local_11b ||
                        ((local_110 <= local_11b || (local_10f <= local_11b)))) ||
                       (local_10e <= local_11b)) ||
                      (((((local_10d <= local_11b || (local_10c <= local_11b)) ||
                          (local_10b <= local_11b)) ||
                         (((local_10a <= local_11b || (local_109 <= local_11b)) ||
                           ((local_108 <= local_11b ||
                             ((local_107 <= local_11b || (local_106 <= local_11b)))))))) ||
                        (local_11b <= local_105)))) ||
                     ((((((((local_104 <= local_11b || (local_103 <= local_11b)) ||
                            (local_102 <= local_11b)) ||
                           ((local_101 <= local_11b || (local_100 <= local_11b)))) ||
                          (local_11b <= local_ff)) ||
                         ((local_fe <= local_11b || (local_fd <= local_11b)))) ||
                        ((local_fc <= local_11b ||
                          (((local_fb <= local_11b || (local_11b <= local_fa)) ||
                            (local_f9 <= local_11b)))))) ||
                       (((((local_f8 <= local_11b || (local_f7 <= local_11b)) ||
                           (local_f6 <= local_11b)) ||
                          ((local_f5 <= local_11b || (local_f4 <= local_11b)))) ||
                         ((local_f3 <= local_11b ||
                           (((local_f2 <= local_11b || (local_f1 <= local_11b)) ||
                             (local_11b <= local_f0)))))))))) ||
                    ((((local_ef <= local_11b || (local_ee <= local_11b)) ||
                       ((local_ed <= local_11b ||
                         (((local_ec <= local_11b || (local_11b <= local_eb)) ||
                           ((local_ea <= local_11b ||
                             ((((local_e9 <= local_11b || (local_11b <= local_e8)) ||
                                (local_e7 <= local_11b)) ||
                               ((local_11b <= local_e6 || (local_e5 <= local_11b)))))))))))) ||
                      (local_e4 <= local_11b)))))))))) ||
             (((local_e3 <= local_11b || (local_e2 <= local_11b)) ||
               (((local_e1 <= local_11b ||
                  (((local_e0 <= local_11b || (local_11a <= local_128[0])) ||
                    (local_11a <= local_128[1])))) ||
                 (((local_11a <= local_128[2] || (local_11a <= local_128[3])) ||
                   (local_124 <= local_11a)))))))))) ||
          ((((((local_123 <= local_11a || (local_11a <= local_122)) ||
               ((local_11a <= local_121 ||
                 (((local_11a <= local_120 || (local_11f <= local_11a)) ||
                   (local_11a <= local_11e)))))) ||
              ((((local_11a <= local_11d || (local_11a <= local_11c)) ||
                 ((local_11a <= local_11b ||
                   (((local_11a <= local_119 || (local_118 <= local_11a)) ||
                     ((local_11a <= local_117 ||
                       ((((local_11a <= local_116 || (local_11a <= local_115)) ||
                          (local_114 <= local_11a)) ||
                         ((local_11a <= local_113 || (local_112 <= local_11a)))))))))))) ||
                ((local_11a <= local_111 ||
                  (((local_11a <= local_110 || (local_11a <= local_10f)) ||
                    ((((local_11a <= local_10e ||
                        (((local_11a <= local_10d || (local_10c <= local_11a)) ||
                          (local_11a <= local_10b)))) ||
                       (((local_109 <= local_11a || (local_11a <= local_108)) ||
                         (local_11a <= local_107)))) ||
                      ((local_11a <= local_106 || (local_11a <= local_105)))))))))))) ||
             ((((local_104 <= local_11a ||
                 (((local_103 <= local_11a || (local_11a <= local_102)) ||
                   (local_11a <= local_101)))) ||
                ((local_11a <= local_100 || (local_11a <= local_ff)))) ||
               (((local_11a <= local_fe ||
                  ((((local_11a <= local_fd || (local_11a <= local_fc)) ||
                     ((local_11a <= local_fb ||
                       (((((local_11a <= local_fa || (local_11a <= local_f8)) ||
                           (local_11a <= local_f7)) ||
                          ((local_11a <= local_f6 || (local_11a <= local_f5)))) ||
                         (local_11a <= local_f4)))))) ||
                    ((local_f3 <= local_11a || (local_f2 <= local_11a)))))) ||
                 ((local_11a <= local_f1 ||
                   ((((local_11a <= local_f0 || (local_ef <= local_11a)) ||
                      (local_ee <= local_11a)) ||
                     (((((local_11a <= local_ed || (local_11a <= local_ec)) ||
                         ((local_11a <= local_eb ||
                           ((local_ea <= local_11a || (local_11a <= local_e9)))))) ||
                        ((local_11a <= local_e8 ||
                          ((((local_11a <= local_e7 || (local_11a <= local_e6)) ||
                             (local_11a <= local_e5)) ||
                            ((local_e4 <= local_11a || (local_e3 <= local_11a)))))))) ||
                       ((((local_11a <= local_e2 ||
                           ((local_e1 <= local_11a || (local_e0 <= local_11a)))) ||
                          (local_119 <= local_128[0])) ||
                         (((((((local_119 <= local_128[1] || (local_119 <= local_128[2])) ||
                               (local_119 <= local_128[3])) ||
                              ((local_124 <= local_119 || (local_123 <= local_119)))) ||
                             ((local_119 <= local_122 ||
                               ((local_119 <= local_121 || (local_120 <= local_119)))))) ||
                            (local_11f <= local_119)) ||
                           (((local_119 <= local_11e || (local_119 <= local_11d)) ||
                             (local_119 <= local_11c)))))))))))))))))) ||
            ((((((local_119 <= local_11b || (local_11a <= local_119)) ||
                 ((local_118 <= local_119 ||
                   ((local_119 <= local_117 || (local_119 <= local_116)))))) ||
                ((((local_114 <= local_119 ||
                    ((((local_119 <= local_113 || (local_112 <= local_119)) ||
                       (local_119 <= local_111)) ||
                      (((local_110 <= local_119 || (local_119 <= local_10f)) ||
                        ((local_119 <= local_10e ||
                          ((local_10c <= local_119 || (local_119 <= local_10b)))))))))) ||
                   ((((local_10a <= local_119 ||
                       ((((local_109 <= local_119 || (local_119 <= local_108)) ||
                          (local_119 <= local_107)) ||
                         ((local_119 <= local_106 || (local_119 <= local_105)))))) ||
                      ((local_104 <= local_119 ||
                        ((local_103 <= local_119 || (local_119 <= local_102)))))) ||
                     (local_119 <= local_100)))) ||
                  ((((((((local_119 <= local_ff || (local_119 <= local_fe)) ||
                         (local_119 <= local_fd)) ||
                        (((local_119 <= local_fc || (local_119 <= local_fb)) ||
                          ((local_119 <= local_fa ||
                            ((local_f9 <= local_119 || (local_119 <= local_f8)))))))) ||
                       ((local_119 <= local_f7 ||
                         (((local_119 <= local_f6 || (local_119 <= local_f5)) ||
                           (local_f3 <= local_119)))))) ||
                      ((local_f2 <= local_119 || (local_119 <= local_f0)))) ||
                     (((local_ef <= local_119 ||
                        ((local_ee <= local_119 || (local_119 <= local_ec)))) ||
                       (local_119 <= local_eb)))) ||
                    (((((((((local_ea <= local_119 || (local_119 <= local_e9)) ||
                            (local_119 <= local_e8)) ||
                           ((local_119 <= local_e7 || (local_119 <= local_e6)))) ||
                          (local_119 <= local_e5)) ||
                         ((local_e4 <= local_119 || (local_e3 <= local_119)))) ||
                        ((local_119 <= local_e2 ||
                          (((local_e1 <= local_119 || (local_e0 <= local_119)) ||
                            (local_118 <= local_128[0])))))) ||
                       ((((local_118 <= local_128[1] || (local_118 <= local_128[2])) ||
                          (local_118 <= local_128[3])) ||
                         ((local_124 <= local_118 || (local_118 <= local_123)))))) ||
                      ((local_118 <= local_122 ||
                        (((local_118 <= local_121 || (local_118 <= local_120)) ||
                          (local_118 <= local_11f)))))))))))) ||
               ((((local_118 <= local_11e || (local_118 <= local_11d)) ||
                  (local_118 <= local_11c)) ||
                 ((((local_118 <= local_11b || (local_118 <= local_11a)) ||
                    ((local_118 <= local_119 ||
                      ((((local_118 <= local_117 || (local_118 <= local_116)) ||
                         (local_118 <= local_115)) ||
                        ((local_114 <= local_118 || (local_118 <= local_113)))))))) ||
                   ((local_118 <= local_112 ||
                     ((local_118 <= local_111 || (local_118 <= local_110)))))))))) ||
              ((((local_118 <= local_10f ||
                  (((local_118 <= local_10e || (local_118 <= local_10d)) ||
                    (local_118 <= local_10c)))) ||
                 (((local_118 <= local_10b || (local_118 <= local_10a)) ||
                   (local_118 <= local_109)))) ||
                ((((local_118 <= local_108 || (local_118 <= local_107)) ||
                   ((((((local_118 <= local_106 ||
                         (((local_118 <= local_105 || (local_104 <= local_118)) ||
                           (local_103 <= local_118)))) ||
                        ((local_118 <= local_102 || (local_118 <= local_101)))) ||
                       (local_118 <= local_100)) ||
                      ((((local_118 <= local_ff || (local_118 <= local_fe)) ||
                         ((local_118 <= local_fd ||
                           ((((local_118 <= local_fc || (local_118 <= local_fb)) ||
                              (local_118 <= local_fa)) ||
                             ((local_118 <= local_f9 || (local_118 <= local_f8)))))))) ||
                        (local_118 <= local_f7)))) ||
                     ((local_118 <= local_f6 || (local_118 <= local_f5)))))) ||
                  (((local_118 <= local_f4 ||
                     (((local_118 <= local_f2 || (local_118 <= local_f1)) ||
                       (local_118 <= local_f0)))) ||
                    (((local_118 <= local_ef || (local_118 <= local_ee)) || (local_118 <= local_ed)
                      ))))))))))))) ||
((((((((local_118 <= local_ec || (local_118 <= local_eb)) ||
       ((local_118 <= local_ea ||
         (((local_118 <= local_e9 || (local_118 <= local_e8)) ||
           (local_118 <= local_e7)))))) ||
      ((local_118 <= local_e6 || (local_118 <= local_e5)))) ||
     (((((local_e4 <= local_118 ||
          (((((((local_118 <= local_e3 || (local_118 <= local_e2)) ||
                ((local_118 <= local_e1 ||
                  (((((local_e0 <= local_118 || (local_117 <= local_128[0])) ||
                      (local_117 <= local_128[1])) ||
                     ((local_117 <= local_128[2] || (local_117 <= local_128[3])))) ||
                    (local_124 <= local_117)))))) ||
               (((local_123 <= local_117 || (local_117 <= local_122)) ||
                 ((local_117 <= local_121 ||
                   (((((local_120 <= local_117 || (local_11f <= local_117)) ||
                       (local_117 <= local_11e)) ||
                      (((local_117 <= local_11d || (local_117 <= local_11c)) ||
                        ((local_117 <= local_11b ||
                          ((local_11a <= local_117 || (local_119 <= local_117)))))))) ||
                     (local_118 <= local_117)))))))) ||
              (((local_117 <= local_116 || (local_115 <= local_117)) ||
                (local_114 <= local_117)))) ||
             ((((local_117 <= local_113 || (local_112 <= local_117)) ||
                ((((local_117 <= local_111 ||
                    ((local_110 <= local_117 || (local_117 <= local_10f)))) ||
                   (local_117 <= local_10e)) ||
                  (((((local_10d <= local_117 || (local_10c <= local_117)) ||
                      (local_117 <= local_10b)) ||
                     ((local_10a <= local_117 || (local_109 <= local_117)))) ||
                    ((local_117 <= local_108 ||
                      ((local_117 <= local_107 || (local_117 <= local_106)))))))))) ||
               (((local_117 <= local_105 ||
                  ((((local_104 <= local_117 || (local_103 <= local_117)) ||
                     (local_117 <= local_102)) ||
                    (((local_101 <= local_117 || (local_117 <= local_100)) ||
                      ((local_117 <= local_ff ||
                        ((local_117 <= local_fd || (local_117 <= local_fc)))))))))) ||
                 ((((local_117 <= local_fb ||
                     (((local_117 <= local_fa || (local_f9 <= local_117)) ||
                       (local_117 <= local_f7)))) ||
                    (((((((((local_117 <= local_f6 || (local_117 <= local_f5)) ||
                            ((local_f4 <= local_117 ||
                              ((local_f3 <= local_117 || (local_f2 <= local_117)))))) ||
                           (local_f1 <= local_117)) ||
                          (((((local_117 <= local_f0 || (local_ef <= local_117)) ||
                              (local_ee <= local_117)) ||
                             ((local_ed <= local_117 || (local_117 <= local_ec)))) ||
                            ((local_117 <= local_eb ||
                              ((local_ea <= local_117 || (local_117 <= local_e9)))))))) ||
                         ((local_117 <= local_e8 ||
                           ((((local_117 <= local_e6 || (local_117 <= local_e5)) ||
                              (local_e4 <= local_117)) ||
                             (((local_e3 <= local_117 || (local_117 <= local_e2)) ||
                               ((local_e1 <= local_117 ||
                                 ((local_e0 <= local_117 || (local_128[1] <= local_116))))))))))
                         )) || (local_116 <= local_128[2])) ||
                       (((((local_128[3] <= local_116 || (local_124 <= local_116)) ||
                           (local_123 <= local_116)) ||
                          ((local_122 <= local_116 || (local_116 <= local_121)))) ||
                         (((local_120 <= local_116 ||
                            ((local_11f <= local_116 || (local_11e <= local_116)))) ||
                           (local_116 <= local_11d)))))) ||
                      ((((((local_11c <= local_116 || (local_116 <= local_11b)) ||
                           (local_11a <= local_116)) ||
                          ((local_119 <= local_116 || (local_118 <= local_116)))) ||
                         (local_117 <= local_116)) ||
                        (((((local_115 <= local_116 || (local_114 <= local_116)) ||
                            ((local_113 <= local_116 ||
                              (((local_112 <= local_116 || (local_111 <= local_116)) ||
                                (local_110 <= local_116)))))) ||
                           ((local_116 <= local_10f || (local_116 <= local_10e)))) ||
                          (local_10d <= local_116)))))))) ||
                   (((((local_10c <= local_116 || (local_116 <= local_10b)) ||
                       ((local_10a <= local_116 ||
                         (((local_109 <= local_116 || (local_108 <= local_116)) ||
                           (local_116 <= local_107)))))) ||
                      (((local_106 <= local_116 || (local_116 <= local_105)) ||
                        ((local_104 <= local_116 ||
                          (((local_103 <= local_116 || (local_116 <= local_102)) ||
                            ((local_101 <= local_116 ||
                              ((((local_100 <= local_116 || (local_116 <= local_ff)) ||
                                 (local_fe <= local_116)) ||
                                ((local_116 <= local_fd || (local_fc <= local_116))))))))))))))
                     || (local_116 <= local_fb)))))))))) ||
            ((((local_116 <= local_fa || (local_f9 <= local_116)) ||
               ((local_f8 <= local_116 ||
                 (((local_116 <= local_f7 || (local_116 <= local_f6)) ||
                   (local_f5 <= local_116)))))) ||
              ((((local_f4 <= local_116 || (local_f3 <= local_116)) ||
                 (local_f2 <= local_116)) ||
                ((local_f1 <= local_116 || (local_116 <= local_f0)))))))))) ||
         (((((local_ef <= local_116 ||
              (((local_ee <= local_116 || (local_ed <= local_116)) ||
                (local_ec <= local_116)))) ||
             (((local_116 <= local_eb || (local_ea <= local_116)) ||
               ((local_116 <= local_e9 ||
                 (((local_116 <= local_e8 || (local_e7 <= local_116)) ||
                   ((local_116 <= local_e6 ||
                     ((((local_e5 <= local_116 || (local_e4 <= local_116)) ||
                        (local_e3 <= local_116)) ||
                       ((local_e2 <= local_116 || (local_e1 <= local_116)))))))))))))) ||
            (local_e0 <= local_116)) ||
           (((local_115 <= local_128[0] || (local_115 <= local_128[1])) ||
             ((((local_115 <= local_128[2] ||
                 (((local_115 <= local_128[3] || (local_124 <= local_115)) ||
                   (local_123 <= local_115)))) ||
                (((local_115 <= local_122 || (local_115 <= local_121)) ||
                  (local_120 <= local_115)))) ||
               ((local_11f <= local_115 || (local_115 <= local_11e)))))))))) ||
        (((local_115 <= local_11d ||
           (((local_115 <= local_11c || (local_115 <= local_11b)) ||
             (local_11a <= local_115)))) ||
          (((local_118 <= local_115 || (local_115 <= local_117)) ||
            ((local_115 <= local_116 ||
              (((local_114 <= local_115 || (local_115 <= local_113)) ||
                ((local_112 <= local_115 ||
                  (((((((local_115 <= local_111 || (local_110 <= local_115)) ||
                        (local_115 <= local_10f)) ||
                       ((local_115 <= local_10e || (local_10c <= local_115)))) ||
                      (local_115 <= local_10b)) ||
                     ((local_10a <= local_115 || (local_109 <= local_115)))) ||
                    (local_115 <= local_108)))))))))))))) ||
       (((((((((local_115 <= local_107 || (local_115 <= local_106)) ||
               (local_115 <= local_105)) ||
              ((local_104 <= local_115 || (local_103 <= local_115)))) ||
             (local_115 <= local_102)) ||
            (((((local_115 <= local_100 || (local_115 <= local_ff)) ||
                ((local_115 <= local_fe ||
                  (((local_115 <= local_fd || (local_115 <= local_fc)) ||
                    (local_115 <= local_fb)))))) ||
               ((local_115 <= local_fa || (local_f9 <= local_115)))) ||
              (local_115 <= local_f8)))) ||
           (((((((local_115 <= local_f7 || (local_115 <= local_f6)) ||
                 ((local_115 <= local_f5 ||
                   ((((local_f3 <= local_115 || (local_f2 <= local_115)) ||
                      (local_115 <= local_f0)) ||
                     ((local_ef <= local_115 || (local_ee <= local_115)))))))) ||
                ((local_115 <= local_ec ||
                  ((local_115 <= local_eb || (local_ea <= local_115)))))) ||
               (((local_115 <= local_e9 ||
                  (((local_115 <= local_e8 || (local_115 <= local_e7)) ||
                    (local_115 <= local_e6)))) ||
                 (((local_115 <= local_e5 || (local_e4 <= local_115)) ||
                   (local_e3 <= local_115)))))) ||
              ((local_115 <= local_e2 || (local_e1 <= local_115)))) ||
             (((local_e0 <= local_115 ||
                (((local_114 <= local_128[0] || (local_114 <= local_128[1])) ||
                  (local_114 <= local_128[2])))) ||
               (((local_114 <= local_128[3] || (local_124 <= local_114)) ||
                 (local_114 <= local_123)))))))) ||
          (((local_114 <= local_122 || (local_114 <= local_121)) ||
            ((local_114 <= local_120 ||
              ((((local_114 <= local_11f || (local_114 <= local_11e)) ||
                 (local_114 <= local_11d)) ||
                ((local_114 <= local_11c || (local_114 <= local_11b)))))))))) ||
         (((local_114 <= local_11a ||
            ((local_114 <= local_119 || (local_114 <= local_118)))) ||
           ((((local_114 <= local_117 ||
               (((local_114 <= local_116 || (local_114 <= local_115)) ||
                 (local_114 <= local_113)))) ||
              (((local_114 <= local_112 || (local_114 <= local_111)) ||
                (local_114 <= local_110)))) ||
             ((local_114 <= local_10f || (local_114 <= local_10e)))))))))))) ||
    (((((local_114 <= local_10d ||
         (((local_114 <= local_10c || (local_114 <= local_10b)) ||
           (local_114 <= local_10a)))) ||
        ((local_114 <= local_109 || (local_114 <= local_108)))) ||
       ((local_114 <= local_107 ||
         ((((((local_114 <= local_106 || (local_114 <= local_105)) ||
              ((local_104 <= local_114 ||
                (((((local_103 <= local_114 || (local_114 <= local_102)) ||
                    (local_114 <= local_101)) ||
                   ((local_114 <= local_100 || (local_114 <= local_ff)))) ||
                  (local_114 <= local_fe)))))) ||
             ((local_114 <= local_fd || (local_114 <= local_fc)))) ||
            (local_114 <= local_fb)) ||
           (((local_114 <= local_fa || (local_114 <= local_f9)) ||
             (local_114 <= local_f8)))))))) ||
      (((((((local_114 <= local_f7 || (local_114 <= local_f6)) ||
            ((local_114 <= local_f5 ||
              ((local_114 <= local_f4 || (local_114 <= local_f3)))))) ||
           ((local_114 <= local_f2 ||
             (((local_114 <= local_f1 || (local_114 <= local_f0)) ||
               (local_114 <= local_ef)))))) ||
          ((((((local_114 <= local_ee || (local_114 <= local_ed)) ||
               ((((local_114 <= local_ec ||
                   ((local_114 <= local_eb || (local_114 <= local_ea)))) ||
                  (local_114 <= local_e9)) ||
                 (((((local_114 <= local_e8 || (local_114 <= local_e7)) ||
                     (local_114 <= local_e6)) ||
                    ((local_114 <= local_e5 || (local_e4 <= local_114)))) ||
                   ((local_114 <= local_e3 ||
                     ((local_114 <= local_e2 || (local_114 <= local_e1)))))))))) ||
              (local_e0 <= local_114)) ||
             ((((((local_113 <= local_128[0] || (local_128[1] <= local_113)) ||
                  (local_113 <= local_128[2])) ||
                 (((local_113 <= local_128[3] || (local_124 <= local_113)) ||
                   ((local_123 <= local_113 ||
                     ((local_113 <= local_122 || (local_113 <= local_121)))))))) ||
                ((local_120 <= local_113 ||
                  (((local_11f <= local_113 || (local_113 <= local_11e)) ||
                    (local_113 <= local_11d)))))) ||
               (((local_11c <= local_113 || (local_113 <= local_11b)) ||
                 (((local_11a <= local_113 ||
                    ((local_119 <= local_113 || (local_118 <= local_113)))) ||
                   (local_117 <= local_113)))))))) ||
            ((((((local_113 <= local_116 || (local_115 <= local_113)) ||
                 (local_114 <= local_113)) ||
                ((local_112 <= local_113 || (local_111 <= local_113)))) ||
               ((local_110 <= local_113 ||
                 ((local_113 <= local_10f || (local_113 <= local_10e)))))) ||
              ((local_10d <= local_113 ||
                ((((local_10c <= local_113 || (local_113 <= local_10b)) ||
                   (local_10a <= local_113)) ||
                  (((local_109 <= local_113 || (local_113 <= local_108)) ||
                    ((local_113 <= local_107 ||
                      ((local_106 <= local_113 || (local_113 <= local_105)))))))))))))))) ||
         ((((local_104 <= local_113 ||
             (((((local_103 <= local_113 || (local_113 <= local_102)) ||
                 (local_101 <= local_113)) ||
                (((local_113 <= local_100 || (local_113 <= local_ff)) ||
                  (((local_fe <= local_113 ||
                     ((local_113 <= local_fd || (local_fc <= local_113)))) ||
                    (local_113 <= local_fb)))))) ||
               (((((local_113 <= local_fa || (local_f9 <= local_113)) ||
                   (local_f8 <= local_113)) ||
                  ((local_113 <= local_f7 || (local_113 <= local_f6)))) ||
                 (local_113 <= local_f5)))))) ||
            ((((local_f4 <= local_113 || (local_f3 <= local_113)) ||
               ((local_f2 <= local_113 ||
                 (((local_f1 <= local_113 || (local_113 <= local_f0)) ||
                   (local_ef <= local_113)))))) ||
              ((local_ee <= local_113 || (local_ed <= local_113)))))) ||
           (((((local_ec <= local_113 ||
                ((((local_113 <= local_eb || (local_ea <= local_113)) ||
                   ((local_113 <= local_e9 ||
                     (((local_113 <= local_e8 || (local_e7 <= local_113)) ||
                       (local_113 <= local_e6)))))) ||
                  ((local_e5 <= local_113 || (local_e4 <= local_113)))))) ||
               (local_e3 <= local_113)) ||
              ((((local_113 <= local_e2 || (local_e1 <= local_113)) ||
                 ((local_e0 <= local_113 ||
                   ((((local_112 <= local_128[0] || (local_112 <= local_128[1])) ||
                      (local_112 <= local_128[2])) ||
                     ((local_112 <= local_128[3] || (local_124 <= local_112)))))))) ||
                ((local_112 <= local_123 ||
                  ((local_112 <= local_122 || (local_112 <= local_121)))))))) ||
             (((((local_112 <= local_120 ||
                  (((local_112 <= local_11e || (local_112 <= local_11d)) ||
                    (local_112 <= local_11c)))) ||
                 (((local_112 <= local_11b || (local_112 <= local_11a)) ||
                   (local_112 <= local_119)))) ||
                (((local_118 <= local_112 || (local_112 <= local_117)) ||
                  ((local_112 <= local_116 ||
                    (((local_112 <= local_115 || (local_114 <= local_112)) ||
                      (local_112 <= local_113)))))))) ||
               ((((((local_112 <= local_111 || (local_112 <= local_110)) ||
                    ((local_112 <= local_10f ||
                      ((((local_112 <= local_10e || (local_112 <= local_10d)) ||
                         ((local_10c <= local_112 ||
                           ((((local_112 <= local_10b || (local_112 <= local_10a)) ||
                              (local_112 <= local_109)) ||
                             ((local_112 <= local_108 || (local_112 <= local_107)))))))) ||
                        (local_112 <= local_106)))))) ||
                   ((((local_112 <= local_105 || (local_104 <= local_112)) ||
                      (((local_103 <= local_112 ||
                         (((local_112 <= local_102 || (local_112 <= local_101)) ||
                           (local_112 <= local_100)))) ||
                        (((local_112 <= local_ff || (local_112 <= local_fe)) ||
                          (local_112 <= local_fd)))))) ||
                     ((local_112 <= local_fc || (local_112 <= local_fb)))))) ||
                  (((((local_112 <= local_fa ||
                       (((local_112 <= local_f9 || (local_112 <= local_f8)) ||
                         (local_112 <= local_f7)))) ||
                      (((local_112 <= local_f6 || (local_112 <= local_f5)) ||
                        ((local_112 <= local_f4 ||
                          (((local_f3 <= local_112 || (local_112 <= local_f2)) ||
                            ((local_112 <= local_f1 ||
                              ((((((local_112 <= local_f0 || (local_112 <= local_ee)) ||
                                   (local_112 <= local_ed)) ||
                                  ((local_112 <= local_ec || (local_112 <= local_eb)))) ||
                                 (local_112 <= local_ea)) ||
                                ((local_112 <= local_e9 || (local_112 <= local_e8)))))))))))))) ||
                     (local_112 <= local_e7)) ||
                    (((((((local_112 <= local_e6 || (local_112 <= local_e5)) ||
                          (local_e4 <= local_112)) ||
                         ((local_112 <= local_e3 || (local_112 <= local_e2)))) ||
                        (((local_112 <= local_e1 ||
                           ((local_e0 <= local_112 || (local_111 <= local_128[0])))) ||
                          (local_111 <= local_128[1])))) ||
                       (((local_111 <= local_128[2] || (local_111 <= local_128[3])) ||
                         (local_124 <= local_111)))) ||
                      ((((local_123 <= local_111 || (local_111 <= local_122)) ||
                         ((local_111 <= local_121 ||
                           ((local_120 <= local_111 || (local_11f <= local_111)))))) ||
                        ((local_111 <= local_11e ||
                          ((((((local_111 <= local_11d || (local_111 <= local_11c)) ||
                               (local_111 <= local_11b)) ||
                              ((local_11a <= local_111 || (local_119 <= local_111)))) ||
                             ((local_118 <= local_111 ||
                               ((local_117 <= local_111 || (local_111 <= local_116)))))) ||
                            (local_115 <= local_111)))))))))))) ||
                 (((local_114 <= local_111 || (local_111 <= local_113)) ||
                   (local_112 <= local_111)))))))))))) ||
        ((((local_110 <= local_111 || (local_111 <= local_10f)) ||
           ((local_111 <= local_10e ||
             ((local_10d <= local_111 || (local_10c <= local_111)))))) ||
          ((local_111 <= local_10b ||
            (((((local_10a <= local_111 || (local_109 <= local_111)) ||
                (local_111 <= local_108)) ||
               (((local_111 <= local_107 || (local_111 <= local_106)) ||
                 ((local_111 <= local_105 ||
                   ((local_104 <= local_111 || (local_103 <= local_111)))))))) ||
              ((((local_111 <= local_102 ||
                  ((((local_101 <= local_111 || (local_111 <= local_100)) ||
                     (local_111 <= local_ff)) ||
                    ((local_fe <= local_111 || (local_111 <= local_fd)))))) ||
                 (((local_111 <= local_fc ||
                    ((local_111 <= local_fb || (local_111 <= local_fa)))) ||
                   (local_f9 <= local_111)))) ||
                ((((local_f8 <= local_111 || (local_111 <= local_f7)) ||
                   (local_111 <= local_f6)) ||
                  (((local_111 <= local_f5 || (local_f4 <= local_111)) ||
                    ((((((local_f3 <= local_111 ||
                          ((local_f2 <= local_111 || (local_f1 <= local_111)))) ||
                         (local_111 <= local_f0)) ||
                        (((((local_ef <= local_111 || (local_ee <= local_111)) ||
                            (local_ed <= local_111)) ||
                           (((local_111 <= local_eb || (local_ea <= local_111)) ||
                             ((local_111 <= local_e9 ||
                               ((local_111 <= local_e8 || (local_e7 <= local_111)))))))) ||
                          (local_111 <= local_e6)))) ||
                       ((((((local_111 <= local_e5 || (local_e4 <= local_111)) ||
                            (local_e3 <= local_111)) ||
                           ((local_111 <= local_e2 || (local_e1 <= local_111)))) ||
                          (local_e0 <= local_111)) ||
                         ((local_110 <= local_128[0] || (local_110 <= local_128[1])))))) ||
                      ((local_110 <= local_128[2] ||
                        (((local_110 <= local_128[3] || (local_124 <= local_110)) ||
                          (local_123 <= local_110)))))))))))))))))))))))) ||
   ((((((((((local_110 <= local_122 || (local_110 <= local_121)) ||
            (local_120 <= local_110)) ||
           ((local_11f <= local_110 || (local_110 <= local_11e)))) ||
          ((local_110 <= local_11d ||
            (((local_110 <= local_11c || (local_110 <= local_11b)) ||
              (local_11a <= local_110)))))) ||
         (((local_110 <= local_119 || (local_118 <= local_110)) ||
           ((local_110 <= local_117 ||
             (((local_110 <= local_116 || (local_110 <= local_115)) ||
               ((local_114 <= local_110 ||
                 ((((local_110 <= local_113 || (local_112 <= local_110)) ||
                    (local_110 <= local_111)) ||
                   ((local_110 <= local_10f || (local_110 <= local_10e)))))))))))))) ||
        (((local_110 <= local_10d ||
           (((local_10c <= local_110 || (local_110 <= local_10b)) ||
             (((local_10a <= local_110 ||
                (((local_109 <= local_110 || (local_110 <= local_108)) ||
                  (local_110 <= local_107)))) ||
               (((local_110 <= local_106 || (local_110 <= local_105)) ||
                 (local_104 <= local_110)))))))) ||
          ((local_103 <= local_110 || (local_110 <= local_102)))))) ||
       (((((local_110 <= local_101 ||
            (((local_110 <= local_100 || (local_110 <= local_ff)) ||
              (local_110 <= local_fe)))) ||
           (((local_110 <= local_fd || (local_110 <= local_fc)) ||
             ((local_110 <= local_fb ||
               (((local_110 <= local_fa || (local_f9 <= local_110)) ||
                 ((local_110 <= local_f8 ||
                   ((((local_110 <= local_f7 || (local_110 <= local_f6)) ||
                      (local_110 <= local_f5)) ||
                     ((local_110 <= local_f4 || (local_f3 <= local_110)))))))))))))) ||
          ((local_f2 <= local_110 ||
            (((local_110 <= local_f1 || (local_110 <= local_f0)) ||
              ((((((local_ef <= local_110 ||
                    (((local_ee <= local_110 || (local_110 <= local_ed)) ||
                      (local_110 <= local_ec)))) ||
                   (((local_110 <= local_eb || (local_ea <= local_110)) ||
                     (local_110 <= local_e9)))) ||
                  ((local_110 <= local_e8 || (local_110 <= local_e7)))) ||
                 ((local_110 <= local_e6 ||
                   (((local_110 <= local_e5 || (local_e4 <= local_110)) ||
                     (local_e3 <= local_110)))))) ||
                ((((local_110 <= local_e2 || (local_e1 <= local_110)) ||
                   ((local_e0 <= local_110 ||
                     ((((local_128[0] <= local_10f || (local_128[1] <= local_10f)) ||
                        ((local_10f <= local_128[2] ||
                          (((((local_128[3] <= local_10f || (local_124 <= local_10f)) ||
                              (local_123 <= local_10f)) ||
                             ((local_122 <= local_10f || (local_120 <= local_10f)))) ||
                            (local_11f <= local_10f)))))) ||
                       ((local_11e <= local_10f || (local_10f <= local_11d)))))))) ||
                  (local_11c <= local_10f)))))))))) ||
         ((((((local_10f <= local_11b || (local_11a <= local_10f)) ||
              (local_119 <= local_10f)) ||
             (((local_118 <= local_10f || (local_117 <= local_10f)) ||
               ((local_116 <= local_10f ||
                 ((local_115 <= local_10f || (local_114 <= local_10f)))))))) ||
            (((((((local_113 <= local_10f ||
                   ((((local_112 <= local_10f || (local_111 <= local_10f)) ||
                      (local_110 <= local_10f)) ||
                     ((local_10f <= local_10e || (local_10d <= local_10f)))))) ||
                  (((local_10c <= local_10f ||
                     ((local_10a <= local_10f || (local_109 <= local_10f)))) ||
                    (local_108 <= local_10f)))) ||
                 ((((((local_106 <= local_10f || (local_10f <= local_105)) ||
                      (local_104 <= local_10f)) ||
                     ((local_103 <= local_10f || (local_10f <= local_102)))) ||
                    ((local_101 <= local_10f ||
                      ((local_100 <= local_10f || (local_10f <= local_ff)))))) ||
                   (local_fe <= local_10f)))) ||
                ((((local_10f <= local_fd || (local_fc <= local_10f)) ||
                   (local_10f <= local_fa)) ||
                  (((local_f9 <= local_10f || (local_f8 <= local_10f)) ||
                    ((local_10f <= local_f6 ||
                      ((local_f5 <= local_10f || (local_f4 <= local_10f)))))))))) ||
               ((local_f3 <= local_10f ||
                 (((local_f2 <= local_10f || (local_f1 <= local_10f)) ||
                   (local_10f <= local_f0)))))) ||
              ((local_ef <= local_10f || (local_ee <= local_10f)))))) ||
           (((((local_ed <= local_10f ||
                ((local_ec <= local_10f || (local_10f <= local_eb)))) ||
               (local_ea <= local_10f)) ||
              ((((((local_10f <= local_e8 || (local_e7 <= local_10f)) ||
                   (local_10f <= local_e6)) ||
                  ((local_e5 <= local_10f || (local_e4 <= local_10f)))) ||
                 ((local_e3 <= local_10f ||
                   ((local_e2 <= local_10f || (local_e1 <= local_10f)))))) ||
                ((local_e0 <= local_10f ||
                  ((((local_128[0] <= local_10e || (local_128[1] <= local_10e)) ||
                     (local_10e <= local_128[2])) ||
                    (((local_128[3] <= local_10e || (local_124 <= local_10e)) ||
                      ((local_123 <= local_10e ||
                        ((local_122 <= local_10e || (local_121 <= local_10e)))))))))))))) ||
             (((local_120 <= local_10e ||
                (((local_11f <= local_10e || (local_11e <= local_10e)) ||
                  (local_10e <= local_11d)))) ||
               (((local_11c <= local_10e || (local_10e <= local_11b)) ||
                 (((local_11a <= local_10e ||
                    ((local_119 <= local_10e || (local_118 <= local_10e)))) ||
                   (local_117 <= local_10e)))))))))))))) ||
      (((((((local_116 <= local_10e || (local_115 <= local_10e)) ||
            (local_114 <= local_10e)) ||
           ((local_113 <= local_10e || (local_112 <= local_10e)))) ||
          (local_111 <= local_10e)) ||
         ((local_110 <= local_10e || (local_10f <= local_10e)))) ||
        ((local_10d <= local_10e ||
          (((local_10c <= local_10e || (local_10b <= local_10e)) ||
            (local_10a <= local_10e)))))))) ||
     (((((((((((local_109 <= local_10e || (local_108 <= local_10e)) ||
               (local_107 <= local_10e)) ||
              ((local_106 <= local_10e || (local_10e <= local_105)))) ||
             (((local_104 <= local_10e ||
                (((local_103 <= local_10e || (local_101 <= local_10e)) ||
                  (local_100 <= local_10e)))) ||
               (((local_10e <= local_ff || (local_fe <= local_10e)) ||
                 (((local_fc <= local_10e ||
                    (((local_fb <= local_10e || (local_10e <= local_fa)) ||
                      ((local_f9 <= local_10e ||
                        ((((local_f8 <= local_10e || (local_f7 <= local_10e)) ||
                           (local_f5 <= local_10e)) ||
                          ((local_f4 <= local_10e || (local_f3 <= local_10e)))))))))) ||
                   (local_f2 <= local_10e)))))))) ||
            ((((local_f1 <= local_10e || (local_10e <= local_f0)) ||
               ((((local_ef <= local_10e ||
                   (((local_ee <= local_10e || (local_ed <= local_10e)) ||
                     (local_ec <= local_10e)))) ||
                  (((local_10e <= local_eb || (local_ea <= local_10e)) ||
                    (local_e9 <= local_10e)))) ||
                 ((local_10e <= local_e8 || (local_e7 <= local_10e)))))) ||
              ((((((local_10e <= local_e6 ||
                    (((local_e5 <= local_10e || (local_e4 <= local_10e)) ||
                      (local_e3 <= local_10e)))) ||
                   ((local_e2 <= local_10e || (local_e1 <= local_10e)))) ||
                  ((local_e0 <= local_10e ||
                    (((local_10d <= local_128[0] || (local_10d <= local_128[1])) ||
                      ((local_10d <= local_128[2] ||
                        ((((local_10d <= local_128[3] || (local_124 <= local_10d)) ||
                           (local_123 <= local_10d)) ||
                          ((local_10d <= local_122 || (local_10d <= local_121)))))))))))) ||
                 (local_120 <= local_10d)) ||
                (((((local_11f <= local_10d || (local_10d <= local_11e)) ||
                    (((local_10d <= local_11d ||
                       (((local_10d <= local_11c || (local_10d <= local_11b)) ||
                         (local_11a <= local_10d)))) ||
                      (((local_118 <= local_10d || (local_10d <= local_117)) ||
                        (local_10d <= local_116)))))) ||
                   ((local_114 <= local_10d || (local_10d <= local_113)))) ||
                  ((local_112 <= local_10d ||
                    (((local_10d <= local_111 || (local_110 <= local_10d)) ||
                      (local_10d <= local_10f)))))))))))) ||
           ((((local_10d <= local_10e || (local_10c <= local_10d)) ||
              ((local_10d <= local_10b ||
                (((((local_10a <= local_10d || (local_109 <= local_10d)) ||
                    ((local_10d <= local_108 ||
                      (((((local_10d <= local_107 || (local_10d <= local_106)) ||
                          (local_10d <= local_105)) ||
                         ((local_104 <= local_10d || (local_103 <= local_10d)))) ||
                        (local_10d <= local_102)))))) ||
                   ((local_10d <= local_100 || (local_10d <= local_ff)))) ||
                  (local_10d <= local_fe)))))) ||
             (((((local_10d <= local_fd || (local_10d <= local_fc)) ||
                 (local_10d <= local_fb)) ||
                (((local_10d <= local_fa || (local_f9 <= local_10d)) ||
                  ((local_10d <= local_f8 ||
                    ((local_10d <= local_f7 || (local_10d <= local_f6)))))))) ||
               (local_10d <= local_f5)))))) ||
          (((((local_f3 <= local_10d || (local_f2 <= local_10d)) ||
              (local_10d <= local_f0)) ||
             ((local_ef <= local_10d || (local_ee <= local_10d)))) ||
            (((local_10d <= local_ec ||
               ((local_10d <= local_eb || (local_ea <= local_10d)))) ||
              (local_10d <= local_e9)))))) ||
         (((((local_10d <= local_e8 || (local_10d <= local_e7)) ||
             (local_10d <= local_e6)) ||
            ((local_10d <= local_e5 || (local_e4 <= local_10d)))) ||
           ((local_e3 <= local_10d ||
             ((local_10d <= local_e2 || (local_e1 <= local_10d)))))))) ||
        ((local_e0 <= local_10d ||
          (((((local_10c <= local_128[0] || (local_10c <= local_128[1])) ||
              (local_10c <= local_128[2])) ||
             (((local_10c <= local_128[3] || (local_124 <= local_10c)) ||
               ((local_10c <= local_123 ||
                 ((local_10c <= local_122 || (local_10c <= local_121)))))))) ||
            ((local_10c <= local_120 ||
              (((local_10c <= local_11f || (local_10c <= local_11e)) ||
                (local_10c <= local_11d)))))))))) ||
       (((((((local_10c <= local_11c || (local_10c <= local_11b)) ||
             ((local_10c <= local_11a ||
               ((local_10c <= local_119 || (local_118 <= local_10c)))))) ||
            ((local_10c <= local_117 ||
              ((((local_10c <= local_116 || (local_10c <= local_115)) ||
                 (local_114 <= local_10c)) ||
                ((local_10c <= local_113 || (local_10c <= local_112)))))))) ||
           ((local_10c <= local_111 ||
             ((local_10c <= local_110 || (local_10c <= local_10f)))))) ||
          (((local_10c <= local_10e ||
             ((((local_10c <= local_10d || (local_10c <= local_10b)) ||
                (local_10c <= local_10a)) ||
               (((local_10c <= local_109 || (local_10c <= local_108)) ||
                 ((local_10c <= local_107 ||
                   ((local_10c <= local_106 || (local_10c <= local_105)))))))))) ||
            ((local_104 <= local_10c ||
              (((local_103 <= local_10c || (local_10c <= local_102)) ||
                (local_10c <= local_101)))))))) ||
         ((((((((local_10c <= local_100 || (local_10c <= local_ff)) ||
                ((((((local_10c <= local_fe ||
                      ((local_10c <= local_fd || (local_10c <= local_fc)))) ||
                     (local_10c <= local_fb)) ||
                    (((((local_10c <= local_fa || (local_10c <= local_f9)) ||
                        (local_10c <= local_f8)) ||
                       ((local_10c <= local_f7 || (local_10c <= local_f6)))) ||
                      (local_10c <= local_f5)))) ||
                   (((local_10c <= local_f4 || (local_f3 <= local_10c)) ||
                     ((local_10c <= local_f2 ||
                       (((local_10c <= local_f1 || (local_10c <= local_f0)) ||
                         (local_10c <= local_ef)))))))) ||
                  ((((local_10c <= local_ee || (local_10c <= local_ed)) ||
                     ((local_10c <= local_ec ||
                       (((local_10c <= local_eb || (local_10c <= local_ea)) ||
                         ((local_10c <= local_e9 ||
                           (((local_10c <= local_e8 || (local_10c <= local_e7)) ||
                             (local_10c <= local_e6)))))))))) ||
                    ((local_10c <= local_e5 || (local_e4 <= local_10c)))))))) ||
               ((local_10c <= local_e3 ||
                 (((((((local_10c <= local_e2 || (local_10c <= local_e1)) ||
                       ((local_e0 <= local_10c ||
                         ((((local_128[0] <= local_10b || (local_128[1] <= local_10b)) ||
                            (local_10b <= local_128[2])) ||
                           ((local_128[3] <= local_10b || (local_124 <= local_10b)))))))) ||
                      (local_123 <= local_10b)) ||
                     (((local_122 <= local_10b || (local_120 <= local_10b)) ||
                       ((local_11f <= local_10b ||
                         (((local_11e <= local_10b || (local_10b <= local_11d)) ||
                           (local_11c <= local_10b)))))))) ||
                    (((((local_10b <= local_11b || (local_11a <= local_10b)) ||
                        (local_119 <= local_10b)) ||
                       ((local_118 <= local_10b || (local_117 <= local_10b)))) ||
                      (((local_116 <= local_10b ||
                         (((local_115 <= local_10b || (local_114 <= local_10b)) ||
                           (local_113 <= local_10b)))) ||
                        (((local_112 <= local_10b || (local_111 <= local_10b)) ||
                          ((local_110 <= local_10b ||
                            (((local_10b <= local_10e || (local_10d <= local_10b)) ||
                              ((local_10c <= local_10b ||
                                ((((local_10a <= local_10b || (local_109 <= local_10b)) ||
                                   (local_108 <= local_10b)) ||
                                  ((local_106 <= local_10b || (local_10b <= local_105))))))))))))))
                      )))) || (local_104 <= local_10b)))))) ||
              (((local_103 <= local_10b || (local_10b <= local_102)) ||
                (((((local_101 <= local_10b ||
                     (((local_100 <= local_10b || (local_10b <= local_ff)) ||
                       (local_fe <= local_10b)))) ||
                    (((local_10b <= local_fd || (local_fc <= local_10b)) ||
                      (local_10b <= local_fa)))) ||
                   (((local_f9 <= local_10b || (local_f8 <= local_10b)) ||
                     ((local_10b <= local_f6 ||
                       (((local_f5 <= local_10b || (local_f4 <= local_10b)) ||
                         (local_f3 <= local_10b)))))))) ||
                  ((local_f2 <= local_10b || (local_f1 <= local_10b)))))))) ||
             ((((((local_10b <= local_f0 ||
                   ((((local_ef <= local_10b || (local_ee <= local_10b)) ||
                      ((local_ed <= local_10b ||
                        ((((((((local_ec <= local_10b || (local_10b <= local_eb)) ||
                               (local_ea <= local_10b)) ||
                              ((local_10b <= local_e8 || (local_e7 <= local_10b)))) ||
                             (local_10b <= local_e6)) ||
                            ((local_e5 <= local_10b || (local_e4 <= local_10b)))) ||
                           (local_e3 <= local_10b)) ||
                          (((local_e2 <= local_10b || (local_e1 <= local_10b)) ||
                            (local_e0 <= local_10b)))))))) ||
                     ((local_10a <= local_128[0] || (local_10a <= local_128[1])))))) ||
                  (local_10a <= local_128[2])) ||
                 (((local_10a <= local_128[3] || (local_124 <= local_10a)) ||
                   ((local_123 <= local_10a ||
                     (((local_10a <= local_122 || (local_10a <= local_121)) ||
                       (local_10a <= local_120)))))))) ||
                (((local_11f <= local_10a || (local_10a <= local_11e)) ||
                  ((local_10a <= local_11d ||
                    (((local_10a <= local_11c || (local_10a <= local_11b)) ||
                      ((local_10a <= local_119 ||
                        ((((local_118 <= local_10a || (local_10a <= local_117)) ||
                           (local_10a <= local_116)) ||
                          ((local_10a <= local_115 || (local_114 <= local_10a)))))))))))))) ||
               (local_10a <= local_113)))) ||
            ((local_112 <= local_10a || (local_10a <= local_111)))) ||
           ((((local_10a <= local_110 ||
               (((local_10a <= local_10f || (local_10a <= local_10e)) ||
                 (local_10a <= local_10d)))) ||
              (((local_10c <= local_10a || (local_10a <= local_10b)) ||
                (local_109 <= local_10a)))) ||
             ((((((local_10a <= local_108 || (local_10a <= local_107)) ||
                  ((local_10a <= local_106 ||
                    (((local_10a <= local_105 || (local_104 <= local_10a)) ||
                      (local_103 <= local_10a)))))) ||
                 (((local_10a <= local_102 || (local_10a <= local_101)) ||
                   ((local_10a <= local_100 ||
                     ((((((local_10a <= local_ff || (local_10a <= local_fe)) ||
                          ((local_10a <= local_fd ||
                            ((((local_10a <= local_fc || (local_10a <= local_fb)) ||
                               (local_10a <= local_fa)) ||
                              ((local_10a <= local_f8 || (local_10a <= local_f7)))))))) ||
                         (local_10a <= local_f6)) ||
                        ((local_10a <= local_f5 || (local_10a <= local_f4)))) ||
                       ((((local_f3 <= local_10a ||
                           (((local_f2 <= local_10a || (local_10a <= local_f1)) ||
                             (local_10a <= local_f0)))) ||
                          (((local_ef <= local_10a || (local_ee <= local_10a)) ||
                            (local_10a <= local_ed)))) ||
                         ((local_10a <= local_ec || (local_10a <= local_eb)))))))))))) ||
                (((local_ea <= local_10a ||
                   (((local_10a <= local_e9 || (local_10a <= local_e8)) ||
                     (local_10a <= local_e7)))) ||
                  ((((local_10a <= local_e6 || (local_10a <= local_e5)) ||
                     (local_e4 <= local_10a)) ||
                    (((local_e3 <= local_10a || (local_10a <= local_e2)) ||
                      ((local_e1 <= local_10a ||
                        (((((local_e0 <= local_10a || (local_109 <= local_128[0])) ||
                            (local_109 <= local_128[1])) ||
                           ((local_109 <= local_128[2] || (local_109 <= local_128[3])))) ||
                          (local_124 <= local_109)))))))))))) ||
               ((local_109 <= local_122 || (local_109 <= local_121)))))))))))))))) ||
  (((((local_109 <= local_120 ||
       (((((local_11f <= local_109 || (local_109 <= local_11e)) ||
           (local_109 <= local_11d)) ||
          (((local_109 <= local_11c || (local_109 <= local_11b)) ||
            ((local_109 <= local_11a ||
              ((local_109 <= local_119 || (local_118 <= local_109)))))))) ||
         (local_109 <= local_117)))) ||
      ((((local_109 <= local_116 || (local_109 <= local_115)) ||
         (local_114 <= local_109)) ||
        (((local_109 <= local_113 || (local_112 <= local_109)) ||
          ((((local_109 <= local_111 ||
              ((local_109 <= local_110 || (local_109 <= local_10f)))) ||
             (local_109 <= local_10e)) ||
            ((((((local_109 <= local_10d || (local_10c <= local_109)) ||
                 (local_109 <= local_10b)) ||
                ((local_109 <= local_10a || (local_109 <= local_108)))) ||
               ((local_109 <= local_107 ||
                 ((local_109 <= local_106 || (local_109 <= local_105)))))) ||
              (local_104 <= local_109)))))))))) ||
     ((((local_103 <= local_109 || (local_109 <= local_102)) ||
        (local_109 <= local_101)) ||
       (((local_109 <= local_100 || (local_109 <= local_ff)) ||
         ((local_109 <= local_fe || ((local_109 <= local_fd || (local_109 <= local_fc))))
         )))))) ||
    (((local_109 <= local_fb ||
       ((((local_109 <= local_fa || (local_109 <= local_f9)) || (local_109 <= local_f8))
         || (((local_109 <= local_f7 || (local_109 <= local_f6)) ||
              ((local_109 <= local_f5 ||
                ((local_109 <= local_f4 || (local_f3 <= local_109)))))))))) ||
      ((((local_109 <= local_f1 ||
          ((((local_109 <= local_f0 || (local_ef <= local_109)) ||
             (local_109 <= local_ed)) ||
            ((local_109 <= local_ec || (local_109 <= local_eb)))))) ||
         (((local_109 <= local_e9 || ((local_109 <= local_e8 || (local_109 <= local_e7)))
            ) || (local_109 <= local_e6)))) ||
        ((((((local_109 <= local_e5 || (local_e4 <= local_109)) ||
             (local_109 <= local_e3)) ||
            (((local_109 <= local_e2 || (local_109 <= local_e1)) ||
              ((local_e0 <= local_109 ||
                ((local_108 <= local_128[0] || (local_128[1] <= local_108)))))))) ||
           ((local_108 <= local_128[2] ||
             (((local_108 <= local_128[3] || (local_124 <= local_108)) ||
               (local_123 <= local_108)))))) ||
          ((local_108 <= local_121 || (local_120 <= local_108)))))))))))))) ||
(((((local_11f <= local_108 || ((local_11e <= local_108 || (local_108 <= local_11d))))
    || (local_11c <= local_108)) ||
   ((((((local_108 <= local_11b || (local_11a <= local_108)) ||
        (local_119 <= local_108)) ||
       ((local_118 <= local_108 || (local_117 <= local_108)))) ||
      (local_108 <= local_116)) ||
     (((local_115 <= local_108 || (local_114 <= local_108)) ||
       ((local_113 <= local_108 ||
         (((local_112 <= local_108 || (local_111 <= local_108)) ||
           (local_110 <= local_108)))))))))) ||
  ((((local_108 <= local_10f || (local_108 <= local_10e)) || (local_10d <= local_108))
    || (((((local_10c <= local_108 || (local_108 <= local_10b)) ||
           ((local_10a <= local_108 ||
             (((local_109 <= local_108 || (local_108 <= local_107)) ||
               (local_106 <= local_108)))))) ||
          ((local_108 <= local_105 || (local_104 <= local_108)))) ||
         ((local_103 <= local_108 ||
           (((local_108 <= local_102 || (local_101 <= local_108)) ||
             ((local_108 <= local_100 ||
               ((((local_108 <= local_ff || (local_fe <= local_108)) ||
                  (local_108 <= local_fd)) ||
                 ((local_fc <= local_108 || (local_108 <= local_fb)))))))))))))))))))) ||
((((((local_108 <= local_fa || ((local_f9 <= local_108 || (local_f8 <= local_108)))) ||
     ((((local_108 <= local_f7 ||
         (((local_108 <= local_f6 || (local_f4 <= local_108)) || (local_f3 <= local_108)))) ||
        ((((((local_f2 <= local_108 || (local_f1 <= local_108)) || (local_108 <= local_f0)) ||
            ((local_ef <= local_108 || (local_ee <= local_108)))) ||
           (((local_ed <= local_108 ||
              (((local_ec <= local_108 || (local_108 <= local_eb)) || (local_ea <= local_108)))) ||
             (((local_108 <= local_e9 || (local_108 <= local_e8)) ||
               ((local_e7 <= local_108 ||
                 ((((local_108 <= local_e6 || (local_e5 <= local_108)) ||
                    ((local_e4 <= local_108 ||
                      ((((local_e3 <= local_108 || (local_e2 <= local_108)) || (local_e1 <= local_108))
                        || ((local_e0 <= local_108 || (local_128[0] <= local_107)))))))) ||
                   (local_128[1] <= local_107)))))))))) ||
          ((((local_107 <= local_128[2] || (local_128[3] <= local_107)) ||
             ((((local_124 <= local_107 ||
                 (((local_123 <= local_107 || (local_122 <= local_107)) || (local_120 <= local_107))
                 )) || (((local_11f <= local_107 || (local_11e <= local_107)) ||
                         (local_107 <= local_11d)))) ||
               ((local_11c <= local_107 || (local_107 <= local_11b)))))) ||
            (((local_11a <= local_107 ||
               (((local_119 <= local_107 || (local_118 <= local_107)) || (local_117 <= local_107))))
              || (((local_116 <= local_107 || (local_115 <= local_107)) || (local_114 <= local_107))
              )))))))) ||
       (((local_113 <= local_107 || (local_112 <= local_107)) ||
         ((local_111 <= local_107 ||
           ((((((local_110 <= local_107 || (local_107 <= local_10e)) || (local_10d <= local_107))
               || ((local_10c <= local_107 || (local_10a <= local_107)))) ||
              (local_109 <= local_107)) || ((local_108 <= local_107 || (local_106 <= local_107))))))
         )))))) ||
((((((((((((local_107 <= local_105 ||
            (((((((local_104 <= local_107 || (local_103 <= local_107)) ||
                  (local_107 <= local_102)) ||
                 ((local_101 <= local_107 || (local_100 <= local_107)))) ||
                (((local_107 <= local_ff ||
                   ((local_fe <= local_107 || (local_107 <= local_fd)))) ||
                  (local_fc <= local_107)))) ||
               (((local_107 <= local_fa || (local_f9 <= local_107)) || (local_f8 <= local_107)
                 ))) || (((local_107 <= local_f6 || (local_f5 <= local_107)) ||
                          ((local_f4 <= local_107 ||
                            ((local_f3 <= local_107 || (local_f2 <= local_107)))))))))) ||
           (local_f1 <= local_107)) ||
          (((((((local_107 <= local_f0 || (local_ef <= local_107)) || (local_ee <= local_107)
                ) || ((local_ed <= local_107 || (local_ec <= local_107)))) ||
              ((local_107 <= local_eb || ((local_ea <= local_107 || (local_107 <= local_e8))))
              )) || ((local_e7 <= local_107 ||
                      (((local_107 <= local_e6 || (local_e5 <= local_107)) ||
                        (local_e4 <= local_107)))))) ||
            (((local_e3 <= local_107 || (local_e2 <= local_107)) ||
              ((local_e1 <= local_107 ||
                ((local_e0 <= local_107 || (local_106 <= local_128[0])))))))))) ||
         (((local_106 <= local_128[2] ||
            ((((local_106 <= local_128[3] || (local_124 <= local_106)) ||
               (local_123 <= local_106)) ||
              (((local_106 <= local_122 || (local_106 <= local_121)) ||
                ((local_120 <= local_106 ||
                  ((local_11f <= local_106 || (local_106 <= local_11e)))))))))) ||
           (((local_106 <= local_11d ||
              ((((local_106 <= local_11c || (local_106 <= local_11b)) ||
                 (local_11a <= local_106)) ||
                ((local_119 <= local_106 || (local_118 <= local_106)))))) ||
             ((((local_117 <= local_106 ||
                 ((local_106 <= local_116 || (local_115 <= local_106)))) ||
                (local_114 <= local_106)) ||
               (((local_106 <= local_113 || (local_112 <= local_106)) ||
                 (local_111 <= local_106)))))))))) ||
        ((((((((local_110 <= local_106 || (local_106 <= local_10f)) ||
               ((((local_106 <= local_10e ||
                   ((local_10d <= local_106 || (local_10c <= local_106)))) ||
                  (local_106 <= local_10b)) ||
                 (((((local_10a <= local_106 || (local_109 <= local_106)) ||
                     (local_106 <= local_108)) ||
                    (((local_106 <= local_107 || (local_106 <= local_105)) ||
                      ((local_104 <= local_106 ||
                        ((local_103 <= local_106 || (local_106 <= local_102)))))))) ||
                   (local_101 <= local_106)))))) ||
              ((((((((local_106 <= local_100 || (local_106 <= local_ff)) ||
                     (local_fe <= local_106)) ||
                    ((local_106 <= local_fd || (local_106 <= local_fb)))) ||
                   (local_106 <= local_fa)) ||
                  ((local_f9 <= local_106 || (local_f8 <= local_106)))) ||
                 ((local_106 <= local_f7 ||
                   (((local_106 <= local_f6 || (local_106 <= local_f5)) ||
                     (local_f4 <= local_106)))))) ||
                ((((((local_f3 <= local_106 || (local_f2 <= local_106)) ||
                     (local_f1 <= local_106)) ||
                    ((local_106 <= local_f0 || (local_ef <= local_106)))) ||
                   ((local_ee <= local_106 ||
                     (((local_ed <= local_106 || (local_ec <= local_106)) ||
                       (local_106 <= local_eb)))))) ||
                  (((((local_ea <= local_106 || (local_106 <= local_e9)) ||
                      ((local_106 <= local_e8 ||
                        (((local_e7 <= local_106 || (local_106 <= local_e6)) ||
                          ((local_e4 <= local_106 ||
                            ((((local_e3 <= local_106 || (local_106 <= local_e2)) ||
                               (local_e1 <= local_106)) ||
                              ((local_e0 <= local_106 || (local_128[0] <= local_105)))))))))))) ||
                     (local_128[1] <= local_105)) ||
                    ((local_128[3] <= local_105 || (local_124 <= local_105)))))))))) ||
             ((((local_123 <= local_105 ||
                 (((local_122 <= local_105 || (local_121 <= local_105)) ||
                   (local_120 <= local_105)))) ||
                (((local_11f <= local_105 || (local_11e <= local_105)) ||
                  (local_11d <= local_105)))) ||
               ((((local_11c <= local_105 || (local_11b <= local_105)) ||
                  ((local_11a <= local_105 ||
                    (((local_119 <= local_105 || (local_118 <= local_105)) ||
                      (local_117 <= local_105)))))) ||
                 ((local_116 <= local_105 || (local_115 <= local_105)))))))) ||
            ((((((local_114 <= local_105 ||
                  (((local_113 <= local_105 || (local_112 <= local_105)) ||
                    ((local_111 <= local_105 ||
                      ((((local_110 <= local_105 || (local_10f <= local_105)) ||
                         (local_10e <= local_105)) ||
                        ((local_10d <= local_105 || (local_10c <= local_105)))))))))) ||
                 (local_10b <= local_105)) ||
                (((local_10a <= local_105 || (local_109 <= local_105)) ||
                  (((((local_108 <= local_105 ||
                       (((local_107 <= local_105 || (local_106 <= local_105)) ||
                         (local_104 <= local_105)))) ||
                      (((local_103 <= local_105 || (local_102 <= local_105)) ||
                        (local_101 <= local_105)))) ||
                     ((local_100 <= local_105 || (local_fe <= local_105)))) ||
                    ((local_fd <= local_105 ||
                      (((local_fc <= local_105 || (local_fb <= local_105)) ||
                        (local_f9 <= local_105)))))))))) ||
               (((local_f8 <= local_105 || (local_f7 <= local_105)) ||
                 ((local_f6 <= local_105 ||
                   ((((local_f5 <= local_105 || (local_f4 <= local_105)) ||
                      ((local_f3 <= local_105 ||
                        (((((local_f2 <= local_105 || (local_f1 <= local_105)) ||
                            (local_ef <= local_105)) ||
                           ((local_ee <= local_105 || (local_ed <= local_105)))) ||
                          (local_ec <= local_105)))))) ||
                     ((local_ea <= local_105 || (local_e9 <= local_105)))))))))) ||
              (local_e7 <= local_105)))) ||
           (((((local_e5 <= local_105 || (local_e4 <= local_105)) || (local_e3 <= local_105))
              || (((local_e2 <= local_105 || (local_e1 <= local_105)) ||
                   ((local_e0 <= local_105 ||
                     ((local_104 <= local_128[0] || (local_104 <= local_128[1])))))))) ||
             ((local_104 <= local_128[2] ||
               ((((local_104 <= local_128[3] || (local_124 <= local_104)) ||
                  (local_104 <= local_123)) ||
                 ((local_104 <= local_122 || (local_104 <= local_121)))))))))) ||
          (((((((local_104 <= local_120 ||
                 ((local_104 <= local_11f || (local_104 <= local_11e)))) ||
                (local_104 <= local_11d)) ||
               ((((((local_104 <= local_11c || (local_104 <= local_11b)) ||
                    (local_104 <= local_11a)) ||
                   ((local_104 <= local_119 || (local_104 <= local_118)))) ||
                  ((local_104 <= local_117 ||
                    ((local_104 <= local_116 || (local_104 <= local_115)))))) ||
                 (local_104 <= local_114)))) ||
              (((local_104 <= local_113 || (local_104 <= local_112)) ||
                (local_104 <= local_111)))) ||
             ((((local_104 <= local_110 || (local_104 <= local_10f)) ||
                ((local_104 <= local_10e ||
                  ((local_104 <= local_10d || (local_104 <= local_10c)))))) ||
               (((local_104 <= local_10b ||
                  (((local_104 <= local_10a || (local_104 <= local_109)) ||
                    (local_104 <= local_108)))) ||
                 (((local_104 <= local_107 || (local_104 <= local_106)) ||
                   ((local_104 <= local_105 ||
                     ((local_104 <= local_103 || (local_104 <= local_102)))))))))))) ||
            ((((local_104 <= local_101 ||
                (((((local_104 <= local_100 || (local_104 <= local_ff)) ||
                    (local_104 <= local_fe)) ||
                   ((local_104 <= local_fd || (local_104 <= local_fc)))) ||
                  ((local_104 <= local_fb || ((local_104 <= local_fa || (local_104 <= local_f9)))
                    ))))) ||
               (((local_104 <= local_f8 ||
                  ((((local_104 <= local_f7 || (local_104 <= local_f6)) ||
                     (local_104 <= local_f5)) ||
                    (((local_104 <= local_f4 || (local_104 <= local_f3)) ||
                      ((local_104 <= local_f2 ||
                        ((local_104 <= local_f1 || (local_104 <= local_f0)))))))))) ||
                 (local_104 <= local_ef)))) ||
              (((((((((local_104 <= local_ee || (local_104 <= local_ed)) ||
                      (local_104 <= local_ec)) ||
                     ((local_104 <= local_eb || (local_104 <= local_ea)))) ||
                    (((local_104 <= local_e9 ||
                       ((local_104 <= local_e8 || (local_104 <= local_e7)))) ||
                      (local_104 <= local_e6)))) ||
                   (((((((local_104 <= local_e5 || (local_104 <= local_e4)) ||
                         (local_104 <= local_e3)) ||
                        ((local_104 <= local_e2 || (local_104 <= local_e1)))) ||
                       (local_e0 <= local_104)) ||
                      ((local_103 <= local_128[0] || (local_103 <= local_128[1])))) ||
                     ((local_103 <= local_128[2] ||
                       (((local_103 <= local_128[3] || (local_124 <= local_103)) ||
                         (local_103 <= local_123)))))))) ||
                  (((((local_103 <= local_122 || (local_103 <= local_121)) ||
                      (local_103 <= local_120)) ||
                     ((local_103 <= local_11f || (local_103 <= local_11e)))) ||
                    ((local_103 <= local_11d ||
                      (((local_103 <= local_11c || (local_103 <= local_11b)) ||
                        (local_103 <= local_11a)))))))) ||
                 ((((local_103 <= local_119 || (local_103 <= local_118)) ||
                    ((local_103 <= local_117 ||
                      (((local_103 <= local_116 || (local_103 <= local_115)) ||
                        ((local_103 <= local_114 ||
                          ((((local_103 <= local_113 || (local_103 <= local_112)) ||
                             (local_103 <= local_111)) ||
                            ((local_103 <= local_110 || (local_103 <= local_10f)))))))))))) ||
                   (local_103 <= local_10e)))) ||
                ((local_103 <= local_10d || (local_103 <= local_10c)))))))))))) ||
       (((((((local_103 <= local_10b ||
              (((local_103 <= local_10a || (local_103 <= local_109)) ||
                (local_103 <= local_108)))) ||
             (((local_103 <= local_107 || (local_103 <= local_106)) ||
               (local_103 <= local_105)))) ||
            (((local_104 <= local_103 || (local_103 <= local_102)) ||
              ((((local_103 <= local_101 ||
                  (((local_103 <= local_100 || (local_103 <= local_ff)) ||
                    (local_103 <= local_fe)))) ||
                 ((local_103 <= local_fd || (local_103 <= local_fc)))) ||
                (local_103 <= local_fb)))))) ||
           (((((((local_103 <= local_fa || (local_103 <= local_f9)) ||
                 ((local_103 <= local_f8 ||
                   ((((local_103 <= local_f7 || (local_103 <= local_f6)) ||
                      (local_103 <= local_f5)) ||
                     ((local_103 <= local_f4 || (local_103 <= local_f3)))))))) ||
                (local_103 <= local_f2)) ||
               ((local_103 <= local_f1 || (local_103 <= local_f0)))) ||
              ((local_103 <= local_ef ||
                (((local_103 <= local_ee || (local_103 <= local_ed)) || (local_103 <= local_ec))
                )))) || ((((local_103 <= local_eb || (local_103 <= local_ea)) ||
                           (local_103 <= local_e9)) ||
                          ((local_103 <= local_e8 || (local_103 <= local_e7)))))))) ||
          (((((local_103 <= local_e6 ||
               (((local_103 <= local_e5 || (local_103 <= local_e3)) || (local_103 <= local_e2))
               )) || (((local_103 <= local_e1 || (local_e0 <= local_103)) ||
                       ((local_128[0] <= local_102 ||
                         (((local_128[1] <= local_102 || (local_102 <= local_128[2])) ||
                           ((local_128[3] <= local_102 ||
                             (((((local_124 <= local_102 || (local_123 <= local_102)) ||
                                 (local_122 <= local_102)) ||
                                ((local_121 <= local_102 || (local_120 <= local_102)))) ||
                               (local_11f <= local_102)))))))))))) ||
             (((local_11e <= local_102 || (local_102 <= local_11d)) ||
               ((local_11c <= local_102 ||
                 (((((((local_102 <= local_11b || (local_11a <= local_102)) ||
                       (local_119 <= local_102)) ||
                      (((local_118 <= local_102 || (local_117 <= local_102)) ||
                        ((local_116 <= local_102 ||
                          ((local_115 <= local_102 || (local_114 <= local_102)))))))) ||
                     (local_113 <= local_102)) ||
                    (((local_112 <= local_102 || (local_111 <= local_102)) ||
                      (local_110 <= local_102)))) ||
                   (((local_10f <= local_102 || (local_10d <= local_102)) ||
                     (((local_10c <= local_102 ||
                        ((local_10b <= local_102 || (local_10a <= local_102)))) ||
                       (local_109 <= local_102)))))))))))) ||
            (((((((((((local_108 <= local_102 || (local_107 <= local_102)) ||
                      (local_106 <= local_102)) ||
                     ((local_102 <= local_105 || (local_104 <= local_102)))) ||
                    ((local_103 <= local_102 ||
                      ((local_101 <= local_102 || (local_100 <= local_102)))))) ||
                   (local_102 <= local_ff)) ||
                  ((((local_fe <= local_102 || (local_fc <= local_102)) ||
                     (local_fb <= local_102)) ||
                    (((local_102 <= local_fa || (local_f9 <= local_102)) ||
                      ((local_f8 <= local_102 ||
                        ((local_f7 <= local_102 || (local_f5 <= local_102)))))))))) ||
                 (local_f4 <= local_102)) ||
                (((local_f3 <= local_102 || (local_f2 <= local_102)) || (local_f1 <= local_102))
                )) || ((local_102 <= local_f0 || (local_ef <= local_102)))) ||
              (((((local_ee <= local_102 || ((local_ed <= local_102 || (local_ec <= local_102)))
                   ) || (((local_102 <= local_eb ||
                           ((((local_ea <= local_102 || (local_e9 <= local_102)) ||
                              (local_102 <= local_e8)) ||
                             ((local_e7 <= local_102 || (local_102 <= local_e6)))))) ||
                          (((local_e5 <= local_102 ||
                             ((local_e4 <= local_102 || (local_e3 <= local_102)))) ||
                            (local_e2 <= local_102)))))) ||
                 ((((((local_e1 <= local_102 || (local_e0 <= local_102)) ||
                      (local_101 <= local_128[0])) ||
                     (((local_101 <= local_128[1] || (local_101 <= local_128[2])) ||
                       ((local_101 <= local_128[3] ||
                         ((local_124 <= local_101 || (local_123 <= local_101)))))))) ||
                    ((local_101 <= local_122 ||
                      (((local_101 <= local_121 || (local_120 <= local_101)) ||
                        (local_11f <= local_101)))))) ||
                   ((((local_101 <= local_11e || (local_101 <= local_11d)) ||
                      (((local_101 <= local_11c ||
                         ((local_101 <= local_11b || (local_11a <= local_101)))) ||
                        (local_118 <= local_101)))) ||
                     (((((local_101 <= local_117 || (local_101 <= local_116)) ||
                         (local_114 <= local_101)) ||
                        ((local_101 <= local_113 || (local_112 <= local_101)))) ||
                       (local_101 <= local_111)))))))) ||
                (((((local_110 <= local_101 || (local_101 <= local_10f)) ||
                    ((local_101 <= local_10e ||
                      (((local_10c <= local_101 || (local_101 <= local_10b)) ||
                        (local_10a <= local_101)))))) ||
                   ((local_109 <= local_101 || (local_101 <= local_108)))) ||
                  (local_101 <= local_107)))))))))) ||
         (((((local_101 <= local_106 || (local_101 <= local_105)) ||
             ((local_104 <= local_101 ||
               (((local_103 <= local_101 || (local_101 <= local_102)) ||
                 (local_101 <= local_100)))))) ||
            ((((local_101 <= local_ff || (local_101 <= local_fe)) ||
               ((local_101 <= local_fd ||
                 (((local_101 <= local_fc || (local_101 <= local_fb)) ||
                   ((local_101 <= local_fa ||
                     ((((local_f9 <= local_101 || (local_101 <= local_f8)) ||
                        (local_101 <= local_f7)) ||
                       ((local_101 <= local_f6 || (local_101 <= local_f5)))))))))))) ||
              (((local_f3 <= local_101 ||
                 (((local_f2 <= local_101 || (local_101 <= local_f0)) ||
                   ((local_ef <= local_101 ||
                     (((local_ee <= local_101 || (local_101 <= local_ec)) ||
                       (local_101 <= local_eb)))))))) ||
                ((((local_ea <= local_101 || (local_101 <= local_e9)) || (local_101 <= local_e8))
                  || ((local_101 <= local_e7 || (local_101 <= local_e6)))))))))) ||
           (((local_101 <= local_e5 ||
              (((local_e4 <= local_101 || (local_e3 <= local_101)) || (local_101 <= local_e2))))
             || (((((((local_e1 <= local_101 || (local_e0 <= local_101)) ||
                      (((((local_100 <= local_128[0] ||
                           (((local_128[1] <= local_100 || (local_100 <= local_128[2])) ||
                             ((local_124 <= local_100 ||
                               ((((local_123 <= local_100 || (local_122 <= local_100)) ||
                                  (local_100 <= local_121)) ||
                                 ((local_120 <= local_100 || (local_11f <= local_100)))))))))) ||
                          (local_11e <= local_100)) ||
                         (((local_100 <= local_11d || (local_11c <= local_100)) ||
                           ((((local_100 <= local_11b ||
                               (((local_11a <= local_100 || (local_119 <= local_100)) ||
                                 (local_118 <= local_100)))) ||
                              (((local_117 <= local_100 || (local_100 <= local_116)) ||
                                (local_115 <= local_100)))) ||
                             ((local_114 <= local_100 || (local_113 <= local_100)))))))) ||
                        ((local_112 <= local_100 ||
                          (((local_111 <= local_100 || (local_110 <= local_100)) ||
                            (local_100 <= local_10f)))))))) ||
                     ((((local_100 <= local_10e || (local_10d <= local_100)) ||
                        ((local_10c <= local_100 ||
                          (((local_100 <= local_10b || (local_10a <= local_100)) ||
                            ((local_109 <= local_100 ||
                              (((((((local_108 <= local_100 || (local_100 <= local_107)) ||
                                    (local_106 <= local_100)) ||
                                   ((local_100 <= local_105 || (local_104 <= local_100)))) ||
                                  (local_103 <= local_100)) ||
                                 ((local_100 <= local_102 || (local_101 <= local_100)))) ||
                                (local_100 <= local_ff)))))))))) ||
                       (((((((local_fe <= local_100 || (local_100 <= local_fd)) ||
                             (local_fc <= local_100)) ||
                            ((local_100 <= local_fb || (local_100 <= local_fa)))) ||
                           (local_f9 <= local_100)) ||
                          (((((local_f8 <= local_100 || (local_100 <= local_f7)) ||
                              ((local_100 <= local_f6 ||
                                (((local_f5 <= local_100 || (local_f4 <= local_100)) ||
                                  (local_f3 <= local_100)))))) ||
                             ((local_f2 <= local_100 || (local_f1 <= local_100)))) ||
                            (local_100 <= local_f0)))) ||
                         ((((local_ef <= local_100 || (local_ee <= local_100)) ||
                            ((local_ed <= local_100 ||
                              ((((local_ec <= local_100 || (local_100 <= local_eb)) ||
                                 (local_ea <= local_100)) ||
                                ((local_100 <= local_e9 || (local_100 <= local_e8)))))))) ||
                           (local_e7 <= local_100)))))))) ||
                    ((((((local_100 <= local_e6 || (local_e5 <= local_100)) ||
                         (((local_e4 <= local_100 ||
                            (((local_e3 <= local_100 || (local_e2 <= local_100)) ||
                              (local_e1 <= local_100)))) ||
                           (((local_e0 <= local_100 || (local_128[0] <= local_ff)) ||
                             (local_128[1] <= local_ff)))))) ||
                        ((local_128[3] <= local_ff || (local_124 <= local_ff)))) ||
                       ((((local_123 <= local_ff ||
                           (((local_122 <= local_ff || (local_121 <= local_ff)) ||
                             (local_120 <= local_ff)))) ||
                          (((local_11f <= local_ff || (local_11e <= local_ff)) ||
                            ((local_11d <= local_ff ||
                              (((local_11c <= local_ff || (local_11b <= local_ff)) ||
                                ((local_11a <= local_ff ||
                                  ((((local_119 <= local_ff || (local_118 <= local_ff)) ||
                                     (local_117 <= local_ff)) ||
                                    ((local_116 <= local_ff || (local_115 <= local_ff)))))))))))))) ||
                         (local_114 <= local_ff)))) ||
                      ((local_113 <= local_ff || (local_112 <= local_ff)))))) ||
                   (((((local_111 <= local_ff ||
                        (((local_110 <= local_ff || (local_10f <= local_ff)) ||
                          (local_10e <= local_ff)))) ||
                       (((local_10d <= local_ff || (local_10c <= local_ff)) ||
                         (local_10b <= local_ff)))) ||
                      (((local_10a <= local_ff || (local_109 <= local_ff)) ||
                        ((local_108 <= local_ff ||
                          (((local_107 <= local_ff || (local_106 <= local_ff)) ||
                            (local_104 <= local_ff)))))))) ||
                     (((local_103 <= local_ff || (local_102 <= local_ff)) ||
                       (((local_101 <= local_ff ||
                          ((((local_100 <= local_ff || (local_fe <= local_ff)) ||
                             ((local_fd <= local_ff ||
                               (((((local_fc <= local_ff || (local_fb <= local_ff)) ||
                                   (local_f9 <= local_ff)) ||
                                  ((local_f8 <= local_ff || (local_f7 <= local_ff)))) ||
                                 (local_f6 <= local_ff)))))) ||
                            ((local_f5 <= local_ff || (local_f4 <= local_ff)))))) ||
                         ((local_f3 <= local_ff ||
                           (((local_f2 <= local_ff || (local_f1 <= local_ff)) ||
                             (local_ef <= local_ff)))))))))))) ||
                  ((((((((local_ee <= local_ff || (local_ed <= local_ff)) ||
                         ((local_ec <= local_ff ||
                           ((local_ea <= local_ff || (local_e9 <= local_ff)))))) ||
                        ((local_e7 <= local_ff ||
                          (((local_e5 <= local_ff || (local_e4 <= local_ff)) ||
                            (local_e3 <= local_ff)))))) ||
                       (((local_e2 <= local_ff || (local_e1 <= local_ff)) ||
                         ((((((((local_e0 <= local_ff ||
                                 ((local_fe <= local_128[0] || (local_fe <= local_128[1])))) ||
                                (local_fe <= local_128[2])) ||
                               (((((local_fe <= local_128[3] || (local_124 <= local_fe)) ||
                                   (local_123 <= local_fe)) ||
                                  ((local_fe <= local_122 || (local_fe <= local_121)))) ||
                                 ((local_120 <= local_fe ||
                                   ((local_11f <= local_fe || (local_fe <= local_11e)))))))) ||
                              (local_fe <= local_11d)) ||
                             ((((local_fe <= local_11c || (local_fe <= local_11b)) ||
                                (local_11a <= local_fe)) ||
                               (((local_119 <= local_fe || (local_118 <= local_fe)) ||
                                 ((local_fe <= local_116 ||
                                   ((local_115 <= local_fe || (local_114 <= local_fe)))))))))) ||
                            (local_fe <= local_113)) ||
                           (((local_112 <= local_fe || (local_fe <= local_111)) ||
                             (local_110 <= local_fe)))))))) ||
                      (((local_fe <= local_10f || (local_fe <= local_10e)) ||
                        ((local_10d <= local_fe ||
                          ((local_10c <= local_fe || (local_fe <= local_10b)))))))) ||
                     (local_10a <= local_fe)) ||
                    ((((local_109 <= local_fe || (local_fe <= local_108)) ||
                       (local_fe <= local_107)) ||
                      ((local_fe <= local_106 || (local_fe <= local_105)))))))))))))))) ||
      (((((((local_104 <= local_fe || ((local_103 <= local_fe || (local_fe <= local_102))))
            || ((local_101 <= local_fe ||
                 ((((local_fe <= local_100 || (local_fe <= local_ff)) || (local_fe <= local_fd)
                    ) || (((local_fe <= local_fc || (local_fe <= local_fb)) ||
                           ((local_fe <= local_fa ||
                             ((local_f9 <= local_fe || (local_fe <= local_f7)))))))))))) ||
           ((local_fe <= local_f6 ||
             ((((local_fe <= local_f5 || (local_f4 <= local_fe)) || (local_f3 <= local_fe)) ||
               (((local_f2 <= local_fe || (local_f1 <= local_fe)) ||
                 (((local_fe <= local_f0 || ((local_ef <= local_fe || (local_ee <= local_fe))))
                   || (local_ed <= local_fe)))))))))) ||
          (((((((((((local_fe <= local_ec || (local_fe <= local_eb)) || (local_ea <= local_fe)
                    ) || ((local_fe <= local_e9 || (local_fe <= local_e8)))) ||
                  (local_fe <= local_e6)) ||
                 (((local_fe <= local_e5 || (local_e4 <= local_fe)) ||
                   ((local_e3 <= local_fe ||
                     (((local_fe <= local_e2 || (local_e1 <= local_fe)) || (local_e0 <= local_fe)
                       ))))))) || ((local_128[0] <= local_fd || (local_128[1] <= local_fd)))) ||
               (((local_fd <= local_128[2] ||
                  ((((local_128[3] <= local_fd || (local_124 <= local_fd)) ||
                     ((local_123 <= local_fd ||
                       (((local_122 <= local_fd || (local_121 <= local_fd)) ||
                         (local_120 <= local_fd)))))) ||
                    ((local_11f <= local_fd || (local_11e <= local_fd)))))) ||
                 (local_fd <= local_11d)))) ||
              (((local_11c <= local_fd || (local_fd <= local_11b)) ||
                ((local_11a <= local_fd ||
                  ((((local_119 <= local_fd || (local_118 <= local_fd)) ||
                     (local_117 <= local_fd)) ||
                    ((local_116 <= local_fd || (local_115 <= local_fd)))))))))) ||
             ((local_114 <= local_fd || ((local_113 <= local_fd || (local_112 <= local_fd))))))
            || (((local_111 <= local_fd ||
                  (((local_110 <= local_fd || (local_10f <= local_fd)) ||
                    (local_10d <= local_fd)))) ||
                 ((((local_10c <= local_fd || (local_10b <= local_fd)) ||
                    (local_10a <= local_fd)) ||
                   (((local_109 <= local_fd || (local_108 <= local_fd)) ||
                     ((local_107 <= local_fd ||
                       (((local_106 <= local_fd || (local_fd <= local_105)) ||
                         (local_104 <= local_fd)))))))))))))) ||
         (((local_103 <= local_fd || (local_101 <= local_fd)) ||
           ((local_100 <= local_fd ||
             ((((((((local_fd <= local_ff || (local_fe <= local_fd)) ||
                    ((local_fc <= local_fd ||
                      ((((local_fb <= local_fd || (local_fd <= local_fa)) ||
                         (local_f9 <= local_fd)) ||
                        ((local_f8 <= local_fd || (local_f7 <= local_fd)))))))) ||
                   (local_f5 <= local_fd)) || ((local_f4 <= local_fd || (local_f3 <= local_fd))))
                 || (((local_f2 <= local_fd ||
                       (((local_f1 <= local_fd || (local_fd <= local_f0)) ||
                         (local_ef <= local_fd)))) ||
                      (((local_ee <= local_fd || (local_ed <= local_fd)) || (local_ec <= local_fd)
                        ))))) || ((local_fd <= local_eb || (local_ea <= local_fd)))) ||
               ((local_e9 <= local_fd ||
                 (((local_fd <= local_e8 || (local_e7 <= local_fd)) || (local_fd <= local_e6))))))
             )))))) ||
        (((((local_e5 <= local_fd || (local_e4 <= local_fd)) ||
            ((local_e3 <= local_fd ||
              (((local_e2 <= local_fd || (local_e1 <= local_fd)) ||
                ((local_e0 <= local_fd ||
                  ((((((local_fc <= local_128[0] || (local_fc <= local_128[2])) ||
                       (local_fc <= local_128[3])) ||
                      ((local_124 <= local_fc || (local_123 <= local_fc)))) ||
                     (local_fc <= local_122)) ||
                    ((local_fc <= local_121 || (local_120 <= local_fc)))))))))))) ||
           (((((local_11f <= local_fc ||
                (((((local_fc <= local_11e || (local_fc <= local_11d)) ||
                    (local_fc <= local_11c)) ||
                   ((local_fc <= local_11b || (local_11a <= local_fc)))) ||
                  (((local_119 <= local_fc ||
                     ((local_118 <= local_fc || (local_117 <= local_fc)))) ||
                    (local_fc <= local_116)))))) ||
               (((local_115 <= local_fc || (local_114 <= local_fc)) || (local_fc <= local_113)))
               ) || (((local_112 <= local_fc || (local_111 <= local_fc)) ||
                      ((local_110 <= local_fc ||
                        ((local_fc <= local_10f || (local_fc <= local_10e)))))))) ||
             (((((local_10d <= local_fc ||
                  (((((local_10c <= local_fc || (local_fc <= local_10b)) ||
                      (local_10a <= local_fc)) ||
                     ((local_109 <= local_fc || (local_fc <= local_108)))) ||
                    ((local_fc <= local_107 ||
                      ((local_fc <= local_105 || (local_104 <= local_fc)))))))) ||
                 (local_103 <= local_fc)) ||
                ((((local_fc <= local_102 || (local_101 <= local_fc)) || (local_fc <= local_100))
                  || ((local_fc <= local_ff || (local_fe <= local_fc)))))) ||
               ((((local_fc <= local_fd || ((local_fc <= local_fb || (local_fc <= local_fa)))) ||
                  ((local_f9 <= local_fc ||
                    ((((local_f8 <= local_fc || (local_fc <= local_f7)) || (local_fc <= local_f6))
                      || (((local_fc <= local_f5 || (local_f4 <= local_fc)) ||
                           ((local_f3 <= local_fc ||
                             ((local_f2 <= local_fc || (local_f1 <= local_fc)))))))))))) ||
                 ((local_fc <= local_f0 ||
                   (((((local_ef <= local_fc || (local_ee <= local_fc)) || (local_ed <= local_fc))
                      || ((local_ec <= local_fc || (local_fc <= local_eb)))) ||
                     ((local_ea <= local_fc || ((local_fc <= local_e9 || (local_fc <= local_e8))))))
                   )))))))))) ||
          (((((local_e7 <= local_fc ||
               (((local_fc <= local_e6 || (local_e4 <= local_fc)) || (local_e3 <= local_fc))))
              || (((local_fc <= local_e2 || (local_e1 <= local_fc)) ||
                   ((((local_e0 <= local_fc ||
                       ((local_128[0] <= local_fb || (local_128[1] <= local_fb)))) ||
                      (local_fb <= local_128[2])) ||
                     (((((local_128[3] <= local_fb || (local_124 <= local_fb)) ||
                         (local_123 <= local_fb)) ||
                        (((local_122 <= local_fb || (local_120 <= local_fb)) ||
                          ((local_11f <= local_fb ||
                            ((local_11e <= local_fb || (local_fb <= local_11d)))))))) ||
                       (local_11c <= local_fb)))))))) ||
             (((((((((((local_fb <= local_11b || (local_11a <= local_fb)) ||
                       (local_119 <= local_fb)) ||
                      ((local_118 <= local_fb || (local_117 <= local_fb)))) ||
                     (local_116 <= local_fb)) ||
                    ((local_115 <= local_fb || (local_114 <= local_fb)))) ||
                   ((local_113 <= local_fb ||
                     (((local_112 <= local_fb || (local_111 <= local_fb)) ||
                       (local_110 <= local_fb)))))) ||
                  (((((local_fb <= local_10e || (local_10d <= local_fb)) ||
                      (local_10c <= local_fb)) ||
                     ((local_10a <= local_fb || (local_109 <= local_fb)))) ||
                    ((local_108 <= local_fb ||
                      (((local_106 <= local_fb || (local_fb <= local_105)) ||
                        (local_104 <= local_fb)))))))) ||
                 ((local_103 <= local_fb || (local_fb <= local_102)))) || (local_101 <= local_fb)
                ) || ((((local_100 <= local_fb || (local_fb <= local_ff)) ||
                        ((local_fe <= local_fb ||
                          ((((local_fb <= local_fd || (local_fc <= local_fb)) ||
                             (local_fb <= local_fa)) ||
                            ((local_f9 <= local_fb || (local_f8 <= local_fb)))))))) ||
                       ((local_fb <= local_f6 ||
                         ((local_f5 <= local_fb || (local_f4 <= local_fb)))))))))) ||
            (((((local_f3 <= local_fb ||
                 (((local_f2 <= local_fb || (local_f1 <= local_fb)) || (local_fb <= local_f0))))
                || (((local_ef <= local_fb || (local_ee <= local_fb)) || (local_ed <= local_fb)))
                ) || ((((local_ec <= local_fb || (local_fb <= local_eb)) ||
                        ((local_ea <= local_fb ||
                          (((local_fb <= local_e8 || (local_e7 <= local_fb)) ||
                            (local_fb <= local_e6)))))) ||
                       ((local_e5 <= local_fb || (local_e4 <= local_fb)))))) ||
              (local_e3 <= local_fb)))))))))) ||
     ((((((local_e2 <= local_fb || (local_e1 <= local_fb)) ||
          ((local_e0 <= local_fb ||
            ((((local_128[0] <= local_fa || (local_128[1] <= local_fa)) ||
               (local_128[3] <= local_fa)) ||
              ((local_124 <= local_fa || (local_123 <= local_fa)))))))) ||
         ((local_122 <= local_fa || ((local_121 <= local_fa || (local_120 <= local_fa)))))) ||
        ((((local_11f <= local_fa ||
            (((local_11e <= local_fa || (local_11d <= local_fa)) || (local_11c <= local_fa))))
           || (((local_11b <= local_fa || (local_11a <= local_fa)) || (local_119 <= local_fa)))
           ) || ((local_118 <= local_fa || (local_117 <= local_fa)))))) ||
       (((((local_116 <= local_fa ||
            (((local_115 <= local_fa || (local_114 <= local_fa)) || (local_113 <= local_fa))))
           || (((local_112 <= local_fa || (local_111 <= local_fa)) || (local_110 <= local_fa)))
           ) || ((((local_10f <= local_fa || (local_10e <= local_fa)) ||
                   ((local_10d <= local_fa ||
                     (((((local_10c <= local_fa || (local_10b <= local_fa)) ||
                         (local_10a <= local_fa)) ||
                        ((local_109 <= local_fa || (local_108 <= local_fa)))) ||
                       (local_107 <= local_fa)))))) ||
                  ((local_106 <= local_fa || (local_104 <= local_fa)))))) ||
         ((((local_103 <= local_fa ||
             (((local_102 <= local_fa || (local_101 <= local_fa)) || (local_100 <= local_fa))))
            || ((((local_fe <= local_fa || (local_fd <= local_fa)) ||
                  ((local_fc <= local_fa || ((local_fb <= local_fa || (local_f9 <= local_fa))))))
                 || (local_f8 <= local_fa)))) ||
           ((((local_f7 <= local_fa || (local_f6 <= local_fa)) || (local_f5 <= local_fa)) ||
             ((local_f4 <= local_fa || (local_f3 <= local_fa)))))))))))) ||
    (((((((local_f2 <= local_fa || ((local_f1 <= local_fa || (local_ef <= local_fa)))) ||
          (local_ee <= local_fa)) ||
         ((((((local_ed <= local_fa || (local_ec <= local_fa)) || (local_ea <= local_fa)) ||
             ((local_e9 <= local_fa || (local_e7 <= local_fa)))) ||
            ((local_e5 <= local_fa || ((local_e4 <= local_fa || (local_e3 <= local_fa)))))) ||
           (local_e2 <= local_fa)))) ||
        ((((local_e1 <= local_fa || (local_e0 <= local_fa)) || (local_f9 <= local_128[0])) ||
          (((local_f9 <= local_128[1] || (local_f9 <= local_128[2])) ||
            ((local_f9 <= local_128[3] || ((local_124 <= local_f9 || (local_123 <= local_f9)))))
            ))))) ||
       ((((local_f9 <= local_122 ||
           (((local_f9 <= local_121 || (local_f9 <= local_120)) || (local_11f <= local_f9))))
          || ((((local_f9 <= local_11e || (local_f9 <= local_11d)) ||
                ((local_f9 <= local_11c || ((local_f9 <= local_11b || (local_f9 <= local_119))))
                )) || ((local_118 <= local_f9 ||
                        ((((local_f9 <= local_117 || (local_f9 <= local_116)) ||
                           (local_f9 <= local_115)) ||
                          ((local_114 <= local_f9 || (local_f9 <= local_113)))))))))) ||
         (((local_112 <= local_f9 || ((local_f9 <= local_111 || (local_f9 <= local_110)))) ||
           ((local_f9 <= local_10f ||
             ((((local_f9 <= local_10e || (local_f9 <= local_10d)) || (local_10c <= local_f9)) ||
               (((local_f9 <= local_10b || (local_109 <= local_f9)) ||
                 ((local_f9 <= local_108 || ((local_f9 <= local_107 || (local_f9 <= local_106))))))
               )))))))))) ||
      ((((((local_f9 <= local_105 ||
            (((local_104 <= local_f9 || (local_103 <= local_f9)) || (local_f9 <= local_102))))
           || ((local_f9 <= local_101 || (local_f9 <= local_100)))) ||
          (((local_f9 <= local_ff || ((local_f9 <= local_fe || (local_f9 <= local_fd)))) ||
            (local_f9 <= local_fc)))) ||
         ((((((((((((local_f9 <= local_fb || (local_f9 <= local_fa)) || (local_f9 <= local_f8))
                   || ((local_f9 <= local_f7 || (local_f9 <= local_f6)))) ||
                  (local_f9 <= local_f5)) || ((local_f9 <= local_f4 || (local_f3 <= local_f9))))
                || ((local_f2 <= local_f9 ||
                     (((local_f9 <= local_f1 || (local_f9 <= local_f0)) || (local_ef <= local_f9)
                       ))))) ||
               ((((((local_ee <= local_f9 || (local_f9 <= local_ed)) || (local_f9 <= local_ec))
                   || ((local_f9 <= local_eb || (local_ea <= local_f9)))) ||
                  ((local_f9 <= local_e9 ||
                    (((local_f9 <= local_e8 || (local_f9 <= local_e7)) || (local_f9 <= local_e6)))
                    ))) || (((local_f9 <= local_e5 || (local_e4 <= local_f9)) ||
                             ((local_e3 <= local_f9 ||
                               (((local_f9 <= local_e2 || (local_e1 <= local_f9)) ||
                                 ((local_e0 <= local_f9 ||
                                   ((((local_f8 <= local_128[0] || (local_f8 <= local_128[1])) ||
                                      (local_f8 <= local_128[2])) ||
                                     ((local_f8 <= local_128[3] || (local_124 <= local_f8))))))))))))))
               )) || ((local_123 <= local_f8 ||
                       ((local_f8 <= local_122 || (local_f8 <= local_121)))))) ||
             ((((((local_120 <= local_f8 ||
                   (((local_11f <= local_f8 || (local_f8 <= local_11e)) ||
                     (local_f8 <= local_11d)))) ||
                  (((local_f8 <= local_11c || (local_f8 <= local_11b)) || (local_11a <= local_f8)
                    ))) || ((local_119 <= local_f8 || (local_118 <= local_f8)))) ||
                ((local_f8 <= local_116 ||
                  (((local_115 <= local_f8 || (local_114 <= local_f8)) || (local_f8 <= local_113))
                  )))) || ((((local_112 <= local_f8 || (local_f8 <= local_111)) ||
                             ((local_110 <= local_f8 ||
                               (((local_f8 <= local_10f || (local_f8 <= local_10e)) ||
                                 ((local_10d <= local_f8 ||
                                   ((((local_10c <= local_f8 || (local_f8 <= local_10b)) ||
                                      (local_10a <= local_f8)) ||
                                     ((local_109 <= local_f8 || (local_f8 <= local_108)))))))))))) ||
                            (local_f8 <= local_107)))))) ||
            (((((local_f8 <= local_106 || (local_f8 <= local_105)) ||
                ((((((local_104 <= local_f8 ||
                      (((local_103 <= local_f8 || (local_f8 <= local_102)) ||
                        (local_101 <= local_f8)))) ||
                     (((local_f8 <= local_100 || (local_f8 <= local_ff)) || (local_f8 <= local_fd)
                       ))) || (((local_f8 <= local_fc || (local_f8 <= local_fb)) ||
                                ((local_f8 <= local_fa ||
                                  (((local_f9 <= local_f8 || (local_f8 <= local_f7)) ||
                                    (local_f8 <= local_f6)))))))) ||
                   ((local_f8 <= local_f5 || (local_f4 <= local_f8)))) ||
                  (((local_f3 <= local_f8 ||
                     ((((local_f2 <= local_f8 || (local_f1 <= local_f8)) ||
                        ((local_f8 <= local_f0 ||
                          (((((local_ef <= local_f8 || (local_ee <= local_f8)) ||
                              (local_ed <= local_f8)) ||
                             ((local_f8 <= local_ec || (local_f8 <= local_eb)))) ||
                            (local_ea <= local_f8)))))) ||
                       ((local_f8 <= local_e9 || (local_f8 <= local_e8)))))) ||
                    (local_f8 <= local_e6)))))) ||
               (((((((((local_f8 <= local_e5 || (local_e4 <= local_f8)) || (local_e3 <= local_f8)
                       ) || (((local_f8 <= local_e2 || (local_e1 <= local_f8)) ||
                              ((local_e0 <= local_f8 ||
                                ((local_128[0] <= local_f7 || (local_128[1] <= local_f7)))))))) ||
                     (local_f7 <= local_128[2])) ||
                    (((local_128[3] <= local_f7 || (local_124 <= local_f7)) ||
                      (local_123 <= local_f7)))) ||
                   (((local_122 <= local_f7 || (local_120 <= local_f7)) ||
                     (((local_11f <= local_f7 ||
                        ((local_11e <= local_f7 || (local_f7 <= local_11d)))) ||
                       (local_11c <= local_f7)))))) ||
                  (((((local_f7 <= local_11b || (local_11a <= local_f7)) ||
                      (local_119 <= local_f7)) ||
                     ((local_118 <= local_f7 || (local_117 <= local_f7)))) ||
                    ((local_116 <= local_f7 || ((local_115 <= local_f7 || (local_114 <= local_f7)))
                      ))))) ||
                 ((local_113 <= local_f7 ||
                   ((((local_112 <= local_f7 || (local_111 <= local_f7)) || (local_110 <= local_f7)
                      ) || (((local_f7 <= local_10e || (local_10d <= local_f7)) ||
                             ((local_10c <= local_f7 ||
                               ((local_10a <= local_f7 || (local_109 <= local_f7)))))))))))))) ||
              ((((((local_108 <= local_f7 ||
                    (((((local_106 <= local_f7 || (local_f7 <= local_105)) ||
                        (local_104 <= local_f7)) ||
                       ((local_103 <= local_f7 || (local_f7 <= local_102)))) ||
                      ((local_101 <= local_f7 ||
                        ((local_100 <= local_f7 || (local_f7 <= local_ff)))))))) ||
                   (((local_fe <= local_f7 ||
                      ((((local_f7 <= local_fd || (local_fc <= local_f7)) || (local_f7 <= local_fa)
                         ) || ((local_f9 <= local_f7 || (local_f8 <= local_f7)))))) ||
                     (((local_f7 <= local_f6 || ((local_f5 <= local_f7 || (local_f4 <= local_f7))))
                       || (local_f3 <= local_f7)))))) ||
                  ((((((local_f2 <= local_f7 || (local_f1 <= local_f7)) || (local_f7 <= local_f0))
                      || (((local_ef <= local_f7 || (local_ee <= local_f7)) ||
                           ((local_ed <= local_f7 ||
                             ((local_ec <= local_f7 || (local_f7 <= local_eb)))))))) ||
                     ((local_ea <= local_f7 ||
                       (((local_f7 <= local_e8 || (local_e7 <= local_f7)) || (local_f7 <= local_e6))
                       )))) || ((((((local_e5 <= local_f7 || (local_e4 <= local_f7)) ||
                                    ((((local_e3 <= local_f7 ||
                                        ((local_e2 <= local_f7 || (local_e1 <= local_f7)))) ||
                                       (local_e0 <= local_f7)) ||
                                      (((((local_128[0] <= local_f6 || (local_128[1] <= local_f6)) ||
                                          (local_f6 <= local_128[2])) ||
                                         ((local_128[3] <= local_f6 || (local_124 <= local_f6)))) ||
                                        (local_123 <= local_f6)))))) ||
                                   (((local_122 <= local_f6 || (local_121 <= local_f6)) ||
                                     ((local_120 <= local_f6 ||
                                       (((local_11f <= local_f6 || (local_11e <= local_f6)) ||
                                         (local_f6 <= local_11d)))))))) ||
                                  ((local_11c <= local_f6 || (local_f6 <= local_11b)))) ||
                                 (local_11a <= local_f6)))))) ||
                 ((((((local_119 <= local_f6 || (local_118 <= local_f6)) ||
                      ((local_117 <= local_f6 ||
                        (((local_116 <= local_f6 || (local_115 <= local_f6)) ||
                          (local_114 <= local_f6)))))) ||
                     (((local_113 <= local_f6 || (local_112 <= local_f6)) ||
                       ((local_111 <= local_f6 ||
                         ((((local_110 <= local_f6 || (local_10f <= local_f6)) ||
                            ((local_10d <= local_f6 ||
                              ((((local_10c <= local_f6 || (local_10b <= local_f6)) ||
                                 (local_10a <= local_f6)) ||
                                ((local_109 <= local_f6 || (local_108 <= local_f6)))))))) ||
                           (local_107 <= local_f6)))))))) ||
                    ((local_106 <= local_f6 || (local_f6 <= local_105)))) ||
                   (((local_104 <= local_f6 ||
                      (((local_103 <= local_f6 || (local_101 <= local_f6)) ||
                        (local_100 <= local_f6)))) ||
                     (((local_f6 <= local_ff || (local_fe <= local_f6)) || (local_fc <= local_f6))))
                   )))) || (((local_fb <= local_f6 || (local_f6 <= local_fa)) ||
                             ((local_f9 <= local_f6 ||
                               (((local_f8 <= local_f6 || (local_f7 <= local_f6)) ||
                                 (local_f5 <= local_f6)))))))))))) ||
           (((((local_f4 <= local_f6 || (local_f3 <= local_f6)) ||
               ((local_f2 <= local_f6 ||
                 ((((local_f1 <= local_f6 || (local_f6 <= local_f0)) ||
                    ((local_ef <= local_f6 ||
                      ((((local_ee <= local_f6 || (local_ed <= local_f6)) || (local_ec <= local_f6))
                        || ((local_f6 <= local_eb || (local_ea <= local_f6)))))))) ||
                   ((local_e9 <= local_f6 || ((local_f6 <= local_e8 || (local_e7 <= local_f6)))))))
                 ))) || (((((local_f6 <= local_e6 ||
                             (((local_e5 <= local_f6 || (local_e4 <= local_f6)) ||
                               (local_e3 <= local_f6)))) ||
                            (((local_e2 <= local_f6 || (local_e1 <= local_f6)) ||
                              (local_e0 <= local_f6)))) ||
                           (((local_f5 <= local_128[0] || (local_128[1] <= local_f5)) ||
                             ((local_f5 <= local_128[2] ||
                               (((local_f5 <= local_128[3] || (local_124 <= local_f5)) ||
                                 (local_123 <= local_f5)))))))) ||
                          (((local_f5 <= local_121 || (local_120 <= local_f5)) ||
                            (local_11f <= local_f5)))))) ||
             (((((local_11e <= local_f5 || (local_f5 <= local_11d)) ||
                 ((local_11c <= local_f5 ||
                   (((((((local_f5 <= local_11b || (local_11a <= local_f5)) ||
                         (local_119 <= local_f5)) ||
                        ((local_118 <= local_f5 || (local_117 <= local_f5)))) ||
                       (local_f5 <= local_116)) ||
                      ((local_115 <= local_f5 || (local_114 <= local_f5)))) ||
                     (local_113 <= local_f5)))))) ||
                ((((local_112 <= local_f5 || (local_111 <= local_f5)) || (local_110 <= local_f5))
                  || ((local_f5 <= local_10f || (local_f5 <= local_10e)))))) ||
               (local_10d <= local_f5)))))))) ||
        ((((((((local_10c <= local_f5 || (local_f5 <= local_10b)) ||
               ((local_10a <= local_f5 ||
                 (((local_109 <= local_f5 || (local_f5 <= local_107)) || (local_106 <= local_f5))
                 )))) || ((((local_f5 <= local_105 || (local_104 <= local_f5)) ||
                            ((local_103 <= local_f5 ||
                              ((((local_f5 <= local_102 || (local_101 <= local_f5)) ||
                                 ((local_f5 <= local_100 ||
                                   ((((local_f5 <= local_ff || (local_fe <= local_f5)) ||
                                      (local_f5 <= local_fd)) ||
                                     ((local_fc <= local_f5 || (local_f5 <= local_fb)))))))) ||
                                (local_f5 <= local_fa)))))) ||
                           ((local_f9 <= local_f5 || (local_f8 <= local_f5)))))) ||
             (((((local_f5 <= local_f7 ||
                  (((local_f5 <= local_f6 || (local_f4 <= local_f5)) || (local_f3 <= local_f5))))
                 || (((local_f2 <= local_f5 || (local_f1 <= local_f5)) || (local_f5 <= local_f0))
                 )) || (((local_ef <= local_f5 || (local_ee <= local_f5)) ||
                         ((local_ed <= local_f5 ||
                           (((local_ec <= local_f5 || (local_f5 <= local_eb)) ||
                             (local_ea <= local_f5)))))))) ||
               ((local_f5 <= local_e9 || (local_f5 <= local_e8)))))) ||
            (((local_e7 <= local_f5 ||
               ((((local_f5 <= local_e6 || (local_e5 <= local_f5)) ||
                  ((local_e4 <= local_f5 ||
                    ((((local_e3 <= local_f5 || (local_e2 <= local_f5)) || (local_e1 <= local_f5))
                      || ((local_e0 <= local_f5 || (local_f4 <= local_128[0])))))))) ||
                 ((local_f4 <= local_128[1] ||
                   ((local_f4 <= local_128[2] || (local_f4 <= local_128[3])))))))) ||
              (((((local_124 <= local_f4 ||
                   (((local_123 <= local_f4 || (local_f4 <= local_122)) || (local_f4 <= local_121)
                     ))) || (((local_120 <= local_f4 || (local_11f <= local_f4)) ||
                              (local_f4 <= local_11e)))) ||
                 ((local_f4 <= local_11d || (local_f4 <= local_11c)))) ||
                ((local_f4 <= local_11b ||
                  (((local_11a <= local_f4 || (local_118 <= local_f4)) || (local_f4 <= local_117)))
                  ))))))) ||
           (((((((local_f4 <= local_116 || (local_114 <= local_f4)) || (local_f4 <= local_113))
                || (((local_112 <= local_f4 || (local_f4 <= local_111)) ||
                     ((local_110 <= local_f4 ||
                       (((((local_f4 <= local_10f || (local_f4 <= local_10e)) ||
                           (local_10c <= local_f4)) ||
                          ((local_f4 <= local_10b || (local_10a <= local_f4)))) ||
                         (local_109 <= local_f4)))))))) ||
               ((local_f4 <= local_108 || (local_f4 <= local_107)))) ||
              (((local_f4 <= local_106 ||
                 (((local_f4 <= local_105 || (local_104 <= local_f4)) || (local_103 <= local_f4)))
                 ) || ((((local_f4 <= local_102 || (local_f4 <= local_100)) ||
                         ((local_f4 <= local_ff ||
                           ((local_f4 <= local_fe || (local_f4 <= local_fd)))))) ||
                        (local_f4 <= local_fc)))))) ||
             (((((local_f4 <= local_fb || (local_f4 <= local_fa)) || (local_f9 <= local_f4)) ||
                (((local_f4 <= local_f8 || (local_f4 <= local_f7)) ||
                  (((local_f4 <= local_f6 || ((local_f4 <= local_f5 || (local_f3 <= local_f4)))) ||
                    (local_f2 <= local_f4)))))) ||
               (((((local_f4 <= local_f0 || (local_ef <= local_f4)) || (local_ee <= local_f4)) ||
                  ((local_f4 <= local_ec || (local_f4 <= local_eb)))) ||
                 ((local_ea <= local_f4 || ((local_f4 <= local_e9 || (local_f4 <= local_e8)))))))))
             ))) || ((local_f4 <= local_e7 ||
                      ((((((local_f4 <= local_e6 || (local_f4 <= local_e5)) ||
                           (local_e4 <= local_f4)) ||
                          (((local_e3 <= local_f4 || (local_f4 <= local_e2)) ||
                            ((local_e1 <= local_f4 ||
                              ((local_e0 <= local_f4 || (local_f3 <= local_128[0])))))))) ||
                         (local_f3 <= local_128[1])) ||
                        (((local_f3 <= local_128[2] || (local_f3 <= local_128[3])) ||
                          (local_124 <= local_f3)))))))))))))) ||
   (((((((local_f3 <= local_123 || (local_f3 <= local_122)) ||
         ((local_f3 <= local_121 || ((local_f3 <= local_120 || (local_f3 <= local_11f)))))) ||
        ((local_f3 <= local_11e ||
          ((((local_f3 <= local_11d || (local_f3 <= local_11c)) || (local_f3 <= local_11b)) ||
            ((local_f3 <= local_11a || (local_f3 <= local_119)))))))) ||
       (((((local_f3 <= local_117 || ((local_f3 <= local_116 || (local_f3 <= local_115)))) ||
           (local_114 <= local_f3)) ||
          ((((local_f3 <= local_113 || (local_f3 <= local_112)) || (local_f3 <= local_111)) ||
            (((local_f3 <= local_110 || (local_f3 <= local_10f)) ||
              ((local_f3 <= local_10e || ((local_f3 <= local_10d || (local_f3 <= local_10c)))))))
            ))) || ((local_f3 <= local_10b ||
                     (((local_f3 <= local_10a || (local_f3 <= local_109)) ||
                       (local_f3 <= local_108)))))))) ||
      (((local_f3 <= local_107 || (local_f3 <= local_106)) ||
        ((((local_f3 <= local_105 || ((local_104 <= local_f3 || (local_103 <= local_f3)))) ||
           (local_f3 <= local_102)) ||
          (((((local_f3 <= local_101 || (local_f3 <= local_100)) || (local_f3 <= local_ff)) ||
             ((local_f3 <= local_fe || (local_f3 <= local_fd)))) || (local_f3 <= local_fc))))))))
     || (((((((local_f3 <= local_fb || (local_f3 <= local_fa)) ||
              ((local_f3 <= local_f9 ||
                (((local_f3 <= local_f8 || (local_f3 <= local_f7)) || (local_f3 <= local_f6)))))
              ) || (((local_f3 <= local_f5 || (local_f3 <= local_f4)) || (local_f3 <= local_f2)
                     ))) ||
            (((local_f3 <= local_f1 || (local_f3 <= local_f0)) ||
              ((local_f3 <= local_ef ||
                (((local_f3 <= local_ee || (local_f3 <= local_ed)) || (local_f3 <= local_ec))))))
            )) || ((local_f3 <= local_eb || (local_f3 <= local_ea)))) ||
          ((((((local_f3 <= local_e9 ||
                ((((((local_f3 <= local_e8 || (local_f3 <= local_e7)) ||
                     ((local_f3 <= local_e6 ||
                       ((((local_f3 <= local_e5 || (local_e4 <= local_f3)) ||
                          (local_f3 <= local_e3)) ||
                         ((local_f3 <= local_e2 || (local_f3 <= local_e1)))))))) ||
                    (local_e0 <= local_f3)) ||
                   ((local_f2 <= local_128[0] || (local_f2 <= local_128[1])))) ||
                  ((local_f2 <= local_128[2] ||
                    (((local_f2 <= local_128[3] || (local_124 <= local_f2)) ||
                      (local_f2 <= local_122)))))))) ||
               ((((local_f2 <= local_121 || (local_f2 <= local_120)) || (local_11f <= local_f2))
                 || ((local_f2 <= local_11e || (local_f2 <= local_11d)))))) ||
              ((local_f2 <= local_11c ||
                (((local_f2 <= local_11b || (local_f2 <= local_11a)) || (local_f2 <= local_119)))
                ))) || (((((local_118 <= local_f2 || (local_f2 <= local_117)) ||
                           (local_f2 <= local_116)) ||
                          (((local_f2 <= local_115 || (local_114 <= local_f2)) ||
                            ((local_f2 <= local_113 ||
                              ((((local_112 <= local_f2 || (local_f2 <= local_111)) ||
                                 (local_f2 <= local_110)) ||
                                ((local_f2 <= local_10f || (local_f2 <= local_10e)))))))))) ||
                         (((local_f2 <= local_10d ||
                            ((local_10c <= local_f2 || (local_f2 <= local_10b)))) ||
                           ((((((local_f2 <= local_10a ||
                                 (((local_f2 <= local_108 || (local_f2 <= local_107)) ||
                                   (local_f2 <= local_106)))) ||
                                (((local_f2 <= local_105 || (local_104 <= local_f2)) ||
                                  (local_103 <= local_f2)))) ||
                               ((local_f2 <= local_102 || (local_f2 <= local_101)))) ||
                              ((local_f2 <= local_100 ||
                                (((local_f2 <= local_ff || (local_f2 <= local_fe)) ||
                                  (local_f2 <= local_fd)))))) ||
                             ((local_f2 <= local_fc || (local_f2 <= local_fb)))))))))) ||
            ((local_f2 <= local_fa ||
              ((((((local_f2 <= local_f9 || (local_f2 <= local_f8)) ||
                   ((local_f2 <= local_f7 ||
                     ((((((local_f2 <= local_f6 || (local_f2 <= local_f5)) ||
                          (local_f2 <= local_f4)) ||
                         ((local_f3 <= local_f2 || (local_f2 <= local_f1)))) ||
                        (local_f2 <= local_f0)) ||
                       ((local_ef <= local_f2 || (local_f2 <= local_ed)))))))) ||
                  (local_f2 <= local_ec)) ||
                 (((((local_f2 <= local_eb || (local_f2 <= local_e9)) || (local_f2 <= local_e8))
                    || ((local_f2 <= local_e7 || (local_f2 <= local_e6)))) ||
                   (((local_f2 <= local_e5 || ((local_e4 <= local_f2 || (local_f2 <= local_e3))))
                     || (local_f2 <= local_e2)))))) ||
                ((((local_f2 <= local_e1 || (local_e0 <= local_f2)) || (local_f1 <= local_128[0]))
                  || (((local_f1 <= local_128[1] || (local_f1 <= local_128[2])) ||
                       ((local_f1 <= local_128[3] ||
                         ((local_124 <= local_f1 || (local_123 <= local_f1)))))))))))))))))))) ||
  ((((((((local_f1 <= local_122 ||
          ((((((local_f1 <= local_121 || (local_120 <= local_f1)) || (local_11f <= local_f1))
              || ((local_f1 <= local_11e || (local_f1 <= local_11d)))) ||
             ((local_f1 <= local_11c || ((local_f1 <= local_11b || (local_11a <= local_f1))))))
            || (local_118 <= local_f1)))) ||
         (((local_f1 <= local_117 || (local_f1 <= local_116)) || (local_114 <= local_f1)))) ||
        (((local_f1 <= local_113 || (local_112 <= local_f1)) ||
          ((local_f1 <= local_111 || ((local_110 <= local_f1 || (local_f1 <= local_10f))))))))
       || (local_f1 <= local_10e)) ||
      ((((((local_10c <= local_f1 || (local_f1 <= local_10b)) || (local_10a <= local_f1)) ||
          (((local_109 <= local_f1 || (local_f1 <= local_108)) ||
            ((local_f1 <= local_107 || ((local_f1 <= local_106 || (local_f1 <= local_105))))))))
         || (local_104 <= local_f1)) ||
        (((((local_103 <= local_f1 || (local_f1 <= local_102)) || (local_f1 <= local_100)) ||
           ((local_f1 <= local_ff || (local_f1 <= local_fe)))) ||
          ((local_f1 <= local_fd || ((local_f1 <= local_fc || (local_f1 <= local_fb)))))))))) ||
     ((local_f1 <= local_fa ||
       (((local_f9 <= local_f1 || (local_f1 <= local_f8)) || (local_f1 <= local_f7)))))) ||
    ((((local_f1 <= local_f6 || (local_f1 <= local_f5)) ||
       (((local_f3 <= local_f1 || ((local_f2 <= local_f1 || (local_f1 <= local_f0)))) ||
         (local_ef <= local_f1)))) ||
      (((((((((local_ee <= local_f1 || (local_f1 <= local_ec)) || (local_f1 <= local_eb)) ||
             (((local_ea <= local_f1 || (local_f1 <= local_e9)) ||
               ((local_f1 <= local_e8 || ((local_f1 <= local_e7 || (local_f1 <= local_e6))))))))
            || ((local_f1 <= local_e5 ||
                 ((((((local_e4 <= local_f1 || (local_e3 <= local_f1)) || (local_f1 <= local_e2))
                     || ((local_e1 <= local_f1 || (local_e0 <= local_f1)))) ||
                    (local_128[0] <= local_f0)) ||
                   ((local_128[1] <= local_f0 || (local_128[3] <= local_f0)))))))) ||
           ((((local_124 <= local_f0 ||
               (((local_123 <= local_f0 || (local_122 <= local_f0)) || (local_121 <= local_f0))))
              || (((local_120 <= local_f0 || (local_11f <= local_f0)) || (local_11e <= local_f0))
              )) || ((local_11d <= local_f0 || (local_11c <= local_f0)))))) ||
          (((((local_11b <= local_f0 ||
               (((local_11a <= local_f0 || (local_119 <= local_f0)) || (local_118 <= local_f0))))
              || (((local_117 <= local_f0 || (local_116 <= local_f0)) ||
                   ((local_115 <= local_f0 ||
                     ((((local_114 <= local_f0 || (local_113 <= local_f0)) ||
                        ((local_112 <= local_f0 ||
                          ((((local_111 <= local_f0 || (local_110 <= local_f0)) ||
                             (local_10f <= local_f0)) ||
                            ((local_10e <= local_f0 || (local_10d <= local_f0)))))))) ||
                       (local_10c <= local_f0)))))))) ||
             ((((local_10b <= local_f0 || (local_10a <= local_f0)) ||
                ((((local_109 <= local_f0 ||
                    (((local_108 <= local_f0 || (local_107 <= local_f0)) || (local_106 <= local_f0)
                      ))) || (((local_104 <= local_f0 || (local_103 <= local_f0)) ||
                               (local_102 <= local_f0)))) ||
                  ((local_101 <= local_f0 || (local_100 <= local_f0)))))) ||
               (((local_fe <= local_f0 ||
                  (((local_fd <= local_f0 || (local_fc <= local_f0)) || (local_fb <= local_f0))))
                 || (((local_f9 <= local_f0 || (local_f8 <= local_f0)) || (local_f7 <= local_f0))))
               )))) || ((((local_f6 <= local_f0 || (local_f5 <= local_f0)) ||
                          ((local_f4 <= local_f0 ||
                            ((((local_f3 <= local_f0 || (local_f2 <= local_f0)) ||
                               (local_f1 <= local_f0)) ||
                              ((local_ef <= local_f0 || (local_ee <= local_f0)))))))) ||
                         ((local_ed <= local_f0 ||
                           ((local_ec <= local_f0 || (local_ea <= local_f0)))))))))) ||
         ((((local_e9 <= local_f0 ||
             (((local_e7 <= local_f0 || (local_e5 <= local_f0)) || (local_e4 <= local_f0)))) ||
            (((local_e3 <= local_f0 || (local_e2 <= local_f0)) || (local_e1 <= local_f0)))) ||
           ((local_e0 <= local_f0 || (local_ef <= local_128[0])))))) ||
        (((local_ef <= local_128[1] ||
           (((local_ef <= local_128[2] || (local_ef <= local_128[3])) || (local_124 <= local_ef))
           )) || ((((local_ef <= local_123 || (local_ef <= local_122)) || (local_ef <= local_121)
                    ) || (((((local_ef <= local_120 || (local_ef <= local_11e)) ||
                             ((local_ef <= local_11d ||
                               (((((local_ef <= local_11c || (local_ef <= local_11b)) ||
                                   (local_ef <= local_11a)) ||
                                  ((local_ef <= local_119 || (local_118 <= local_ef)))) ||
                                 (local_ef <= local_117)))))) ||
                            (((local_ef <= local_116 || (local_ef <= local_115)) ||
                              ((local_114 <= local_ef ||
                                (((local_ef <= local_113 || (local_ef <= local_111)) ||
                                  (local_ef <= local_110)))))))) ||
                           ((((((((local_ef <= local_10f || (local_ef <= local_10e)) ||
                                  ((local_ef <= local_10d ||
                                    ((local_10c <= local_ef || (local_ef <= local_10b)))))) ||
                                 (local_ef <= local_10a)) ||
                                ((((local_ef <= local_109 || (local_ef <= local_108)) ||
                                   (local_ef <= local_107)) ||
                                  ((local_ef <= local_106 || (local_ef <= local_105)))))) ||
                               (((local_104 <= local_ef ||
                                  ((local_103 <= local_ef || (local_ef <= local_102)))) ||
                                 (local_ef <= local_101)))) ||
                              (((((((local_ef <= local_100 || (local_ef <= local_ff)) ||
                                    (local_ef <= local_fe)) ||
                                   ((local_ef <= local_fd || (local_ef <= local_fc)))) ||
                                  ((local_ef <= local_fb ||
                                    ((local_ef <= local_fa || (local_ef <= local_f9)))))) ||
                                 (local_ef <= local_f8)) ||
                                ((((local_ef <= local_f7 || (local_ef <= local_f6)) ||
                                   (local_ef <= local_f5)) ||
                                  (((local_ef <= local_f4 || (local_f3 <= local_ef)) ||
                                    ((local_ef <= local_f2 ||
                                      ((local_ef <= local_f1 || (local_ef <= local_f0)))))))))))) ||
                             (((local_ef <= local_ee ||
                                (((local_ef <= local_ed || (local_ef <= local_ec)) ||
                                  (local_ef <= local_eb)))) ||
                               ((local_ef <= local_ea || (local_ef <= local_e9))))))))))))))))))))))
|| ((((((((((local_ef <= local_e8 || ((local_ef <= local_e7 || (local_ef <= local_e6)))) ||
            (local_ef <= local_e5)) ||
           ((((local_e4 <= local_ef || (local_ef <= local_e3)) || (local_ef <= local_e2)) ||
             ((local_ef <= local_e1 || (local_e0 <= local_ef)))))) ||
          (((local_ee <= local_128[0] ||
             ((local_ee <= local_128[1] || (local_ee <= local_128[2])))) ||
            ((local_ee <= local_128[3] ||
              (((((((local_124 <= local_ee || (local_ee <= local_122)) ||
                    (local_ee <= local_121)) ||
                   (((local_ee <= local_120 || (local_11f <= local_ee)) ||
                     ((local_ee <= local_11e ||
                       ((local_ee <= local_11d || (local_ee <= local_11c)))))))) ||
                  (local_ee <= local_11b)) ||
                 (((local_ee <= local_11a || (local_ee <= local_119)) || (local_118 <= local_ee))
                 )) || ((local_ee <= local_117 || (local_ee <= local_116)))))))))) ||
         ((((((local_ee <= local_115 || ((local_114 <= local_ee || (local_ee <= local_113))))
              || (local_112 <= local_ee)) ||
             ((((((((local_ee <= local_111 || (local_ee <= local_110)) ||
                    (local_ee <= local_10f)) ||
                   ((local_ee <= local_10e || (local_ee <= local_10d)))) ||
                  (local_10c <= local_ee)) ||
                 ((local_ee <= local_10b || (local_ee <= local_10a)))) ||
                ((local_ee <= local_108 ||
                  (((local_ee <= local_107 || (local_ee <= local_106)) || (local_ee <= local_105)
                    ))))) ||
               (((local_104 <= local_ee || (local_103 <= local_ee)) || (local_ee <= local_102)))
               ))) || (((((local_ee <= local_101 || (local_ee <= local_100)) ||
                          ((local_ee <= local_ff ||
                            (((local_ee <= local_fe || (local_ee <= local_fd)) ||
                              (local_ee <= local_fc)))))) ||
                         ((local_ee <= local_fb || (local_ee <= local_fa)))) ||
                        (local_ee <= local_f9)))) ||
           ((((local_ee <= local_f8 || (local_ee <= local_f7)) ||
              ((local_ee <= local_f6 ||
                ((((local_ee <= local_f5 || (local_ee <= local_f4)) || (local_f3 <= local_ee)) ||
                  ((local_ee <= local_f1 || (local_ee <= local_f0)))))))) ||
             (local_ef <= local_ee)))))) ||
        (((local_ee <= local_ed || (local_ee <= local_ec)) ||
          ((local_ee <= local_eb ||
            (((local_ee <= local_e9 || (local_ee <= local_e8)) || (local_ee <= local_e7))))))))
       || ((((local_ee <= local_e6 || (local_ee <= local_e5)) || (local_e4 <= local_ee)) ||
            (((local_ee <= local_e3 || (local_ee <= local_e2)) ||
              (((((((local_ee <= local_e1 ||
                     (((local_e0 <= local_ee || (local_ed <= local_128[0])) ||
                       (local_ed <= local_128[1])))) ||
                    ((local_ed <= local_128[2] || (local_ed <= local_128[3])))) ||
                   ((local_124 <= local_ed ||
                     (((local_123 <= local_ed || (local_ed <= local_122)) ||
                       ((local_ed <= local_121 ||
                         ((((local_120 <= local_ed || (local_11f <= local_ed)) ||
                            (local_ed <= local_11e)) ||
                           ((local_ed <= local_11d || (local_ed <= local_11c)))))))))))) ||
                  (local_ed <= local_11b)) ||
                 ((((local_11a <= local_ed || (local_118 <= local_ed)) ||
                    ((local_ed <= local_117 ||
                      (((local_ed <= local_116 || (local_114 <= local_ed)) ||
                        (local_ed <= local_113)))))) ||
                   (((((local_112 <= local_ed || (local_ed <= local_111)) ||
                       (local_110 <= local_ed)) ||
                      ((local_ed <= local_10f || (local_ed <= local_10e)))) ||
                     ((local_10c <= local_ed ||
                       (((local_ed <= local_10b || (local_10a <= local_ed)) ||
                         (local_109 <= local_ed)))))))))) ||
                ((local_ed <= local_108 || (local_ed <= local_107)))))))))) ||
      ((((local_ed <= local_106 ||
          (((local_ed <= local_105 || (local_104 <= local_ed)) ||
            ((local_103 <= local_ed ||
              (((((local_ed <= local_102 || (local_ed <= local_100)) || (local_ed <= local_ff))
                 || ((local_ed <= local_fe || (local_ed <= local_fd)))) || (local_ed <= local_fc))
              )))))) ||
         ((((local_ed <= local_fb || (local_ed <= local_fa)) || (local_f9 <= local_ed)) ||
           (((((local_ed <= local_f8 || (local_ed <= local_f7)) || (local_ed <= local_f6)) ||
              (((local_ed <= local_f5 || (local_f3 <= local_ed)) ||
                ((local_f2 <= local_ed || ((local_ed <= local_f0 || (local_ef <= local_ed))))))))
             || ((local_ee <= local_ed ||
                  (((local_ed <= local_ec || (local_ed <= local_eb)) || (local_ea <= local_ed)))))
             ))))) ||
        (((local_ed <= local_e9 || (local_ed <= local_e8)) ||
          ((((((local_ed <= local_e7 || ((local_ed <= local_e6 || (local_ed <= local_e5)))) ||
               (local_e4 <= local_ed)) ||
              (((((local_e3 <= local_ed || (local_ed <= local_e2)) || (local_e1 <= local_ed)) ||
                 ((local_e0 <= local_ed || (local_ec <= local_128[0])))) ||
                ((local_ec <= local_128[1] ||
                  ((local_ec <= local_128[2] || (local_ec <= local_128[3])))))))) ||
             (local_124 <= local_ec)) ||
            ((((local_123 <= local_ec || (local_ec <= local_122)) || (local_ec <= local_121)) ||
              (((local_120 <= local_ec || (local_11f <= local_ec)) ||
                ((local_ec <= local_11e || ((local_ec <= local_11d || (local_ec <= local_11c)))))))
              ))))))))) ||
     ((((((local_ec <= local_11b ||
           (((local_11a <= local_ec || (local_119 <= local_ec)) || (local_118 <= local_ec))))
          || ((local_117 <= local_ec || (local_ec <= local_116)))) ||
         (((((local_115 <= local_ec || ((local_114 <= local_ec || (local_ec <= local_113)))) ||
             ((local_112 <= local_ec ||
               ((((local_110 <= local_ec || (local_ec <= local_10f)) || (local_ec <= local_10e))
                 || ((local_10d <= local_ec || (local_10c <= local_ec)))))))) ||
            (((local_ec <= local_10b || ((local_10a <= local_ec || (local_109 <= local_ec)))) ||
              ((local_ec <= local_108 ||
                (((((local_ec <= local_107 || (local_ec <= local_106)) || (local_ec <= local_105))
                   || (((local_104 <= local_ec || (local_103 <= local_ec)) ||
                        ((local_ec <= local_102 ||
                          ((local_101 <= local_ec || (local_ec <= local_100)))))))) ||
                  (local_ec <= local_ff)))))))) ||
           ((((((local_fe <= local_ec || (local_ec <= local_fd)) || (local_ec <= local_fc)) ||
               (((local_ec <= local_fb || (local_ec <= local_fa)) ||
                 (((local_f9 <= local_ec || ((local_f8 <= local_ec || (local_ec <= local_f7)))) ||
                   (local_ec <= local_f6)))))) ||
              ((((((local_ec <= local_f5 || (local_f4 <= local_ec)) || (local_f3 <= local_ec)) ||
                  ((local_f2 <= local_ec || (local_f1 <= local_ec)))) || (local_ec <= local_f0))
                || (((local_ef <= local_ec || (local_ee <= local_ec)) ||
                     ((local_ed <= local_ec ||
                       (((local_ec <= local_eb || (local_ea <= local_ec)) || (local_ec <= local_e9))
                       )))))))) ||
             (((((local_ec <= local_e8 || (local_e7 <= local_ec)) ||
                 (((((local_ec <= local_e6 ||
                      (((((local_ec <= local_e5 || (local_e4 <= local_ec)) ||
                          ((local_e3 <= local_ec ||
                            (((local_ec <= local_e2 || (local_e1 <= local_ec)) ||
                              (local_e0 <= local_ec)))))) ||
                         ((local_128[0] <= local_eb || (local_128[1] <= local_eb)))) ||
                        (local_128[3] <= local_eb)))) ||
                     ((((local_124 <= local_eb || (local_123 <= local_eb)) ||
                        ((local_122 <= local_eb ||
                          ((((local_121 <= local_eb || (local_120 <= local_eb)) ||
                             (local_11f <= local_eb)) ||
                            ((local_11e <= local_eb || (local_11d <= local_eb)))))))) ||
                       (local_11c <= local_eb)))) ||
                    (((local_11b <= local_eb || (local_11a <= local_eb)) ||
                      ((local_119 <= local_eb ||
                        (((local_118 <= local_eb || (local_117 <= local_eb)) ||
                          (local_116 <= local_eb)))))))) ||
                   (((local_115 <= local_eb || (local_114 <= local_eb)) || (local_113 <= local_eb))
                   )))) || ((local_112 <= local_eb || (local_111 <= local_eb)))) ||
               (((((local_110 <= local_eb ||
                    (((local_10f <= local_eb || (local_10e <= local_eb)) || (local_10d <= local_eb)
                      ))) || (((local_10c <= local_eb || (local_10b <= local_eb)) ||
                               ((local_10a <= local_eb ||
                                 ((((local_109 <= local_eb || (local_108 <= local_eb)) ||
                                    ((local_107 <= local_eb ||
                                      ((((local_106 <= local_eb || (local_104 <= local_eb)) ||
                                         (local_103 <= local_eb)) ||
                                        ((local_102 <= local_eb || (local_101 <= local_eb)))))))) ||
                                   (local_100 <= local_eb)))))))) ||
                  (((local_fe <= local_eb || (local_fd <= local_eb)) ||
                    (((local_fc <= local_eb ||
                       (((local_fb <= local_eb || (local_f9 <= local_eb)) || (local_f8 <= local_eb)))
                       ) || (((local_f7 <= local_eb || (local_f6 <= local_eb)) ||
                              (local_f5 <= local_eb)))))))) ||
                 ((((local_f4 <= local_eb || (local_f3 <= local_eb)) ||
                    ((local_f2 <= local_eb ||
                      (((local_f1 <= local_eb || (local_ef <= local_eb)) || (local_ee <= local_eb))))
                    )) || ((local_ed <= local_eb || (local_ec <= local_eb)))))))))))))) ||
        ((((local_ea <= local_eb ||
            (((local_e9 <= local_eb || (local_e7 <= local_eb)) ||
              ((local_e5 <= local_eb ||
                (((((((((local_e4 <= local_eb || (local_e3 <= local_eb)) || (local_e2 <= local_eb)
                        ) || ((local_e1 <= local_eb || (local_e0 <= local_eb)))) ||
                      (local_ea <= local_128[0])) ||
                     ((local_ea <= local_128[1] || (local_ea <= local_128[2])))) ||
                    (local_ea <= local_128[3])) ||
                   (((local_124 <= local_ea || (local_ea <= local_122)) || (local_ea <= local_121))
                   )) || ((local_ea <= local_120 || (local_11f <= local_ea)))))))))) ||
           ((local_ea <= local_11e || ((local_ea <= local_11d || (local_ea <= local_11c)))))) ||
          ((((((local_ea <= local_11b ||
                (((local_ea <= local_11a || (local_ea <= local_119)) || (local_118 <= local_ea)))
                ) || (((local_ea <= local_117 || (local_ea <= local_116)) ||
                       (local_ea <= local_115)))) ||
              ((local_114 <= local_ea || (local_ea <= local_113)))) ||
             ((local_112 <= local_ea ||
               ((((local_ea <= local_111 || (local_ea <= local_110)) || (local_ea <= local_10f))
                 || ((local_ea <= local_10e || (local_ea <= local_10d)))))))) ||
            (local_10c <= local_ea)))))) ||
       (((((((local_ea <= local_10b || (local_ea <= local_10a)) ||
             (((local_ea <= local_108 ||
                (((local_ea <= local_107 || (local_ea <= local_106)) || (local_ea <= local_105)))
                ) || (((local_104 <= local_ea || (local_103 <= local_ea)) ||
                       (local_ea <= local_102)))))) ||
            (((local_ea <= local_101 || (local_ea <= local_100)) ||
              (((((local_ea <= local_ff ||
                   (((local_ea <= local_fe || (local_ea <= local_fd)) || (local_ea <= local_fc))))
                  || (((local_ea <= local_fb || (local_ea <= local_fa)) ||
                       ((local_ea <= local_f9 ||
                         (((local_ea <= local_f8 || (local_ea <= local_f7)) ||
                           ((local_ea <= local_f6 ||
                             ((((local_ea <= local_f5 || (local_ea <= local_f4)) ||
                                (local_f3 <= local_ea)) ||
                               ((local_ea <= local_f1 || (local_ea <= local_f0)))))))))))))) ||
                 (local_ef <= local_ea)) ||
                (((local_ea <= local_ed || (local_ea <= local_ec)) ||
                  ((((local_ea <= local_eb ||
                      (((local_ea <= local_e9 || (local_ea <= local_e8)) || (local_ea <= local_e7)))
                      ) || (((local_ea <= local_e6 || (local_ea <= local_e5)) ||
                             (local_e4 <= local_ea)))) ||
                    (((local_ea <= local_e3 || (local_ea <= local_e2)) ||
                      ((local_ea <= local_e1 ||
                        (((local_e0 <= local_ea || (local_128[0] <= local_e9)) ||
                          (local_128[1] <= local_e9)))))))))))))))) ||
           ((local_e9 <= local_128[2] || (local_128[3] <= local_e9)))) ||
          (((((local_124 <= local_e9 ||
               ((((local_123 <= local_e9 || (local_122 <= local_e9)) ||
                  ((local_120 <= local_e9 ||
                    (((((local_11f <= local_e9 || (local_11e <= local_e9)) ||
                        (local_e9 <= local_11d)) ||
                       ((local_11c <= local_e9 || (local_e9 <= local_11b)))) ||
                      (local_11a <= local_e9)))))) ||
                 ((local_119 <= local_e9 || (local_118 <= local_e9)))))) ||
              (local_117 <= local_e9)) ||
             (((((local_116 <= local_e9 || (local_115 <= local_e9)) || (local_114 <= local_e9))
                || (((local_113 <= local_e9 || (local_112 <= local_e9)) ||
                     ((local_111 <= local_e9 ||
                       ((local_110 <= local_e9 || (local_e9 <= local_10e)))))))) ||
               (((local_10d <= local_e9 ||
                  (((local_10c <= local_e9 || (local_10a <= local_e9)) || (local_109 <= local_e9)))
                  ) || (((local_108 <= local_e9 || (local_106 <= local_e9)) ||
                         ((((local_e9 <= local_105 ||
                             ((local_104 <= local_e9 || (local_103 <= local_e9)))) ||
                            (local_e9 <= local_102)) ||
                           ((((((local_101 <= local_e9 || (local_100 <= local_e9)) ||
                                (local_e9 <= local_ff)) ||
                               ((local_fe <= local_e9 || (local_e9 <= local_fd)))) ||
                              ((local_fc <= local_e9 ||
                                ((local_e9 <= local_fa || (local_f9 <= local_e9)))))) ||
                             (local_f8 <= local_e9)))))))))))) ||
            (((((((local_e9 <= local_f6 || (local_f5 <= local_e9)) || (local_f4 <= local_e9)) ||
                 (((local_f3 <= local_e9 || (local_f2 <= local_e9)) ||
                   ((local_f1 <= local_e9 || ((local_e9 <= local_f0 || (local_ef <= local_e9)))))))
                 ) || (local_ee <= local_e9)) ||
               (((local_ed <= local_e9 || (local_ec <= local_e9)) || (local_e9 <= local_eb)))) ||
              ((((local_ea <= local_e9 || (local_e9 <= local_e8)) ||
                 ((local_e7 <= local_e9 || ((local_e9 <= local_e6 || (local_e5 <= local_e9)))))) ||
                (((local_e4 <= local_e9 ||
                   ((((local_e3 <= local_e9 || (local_e2 <= local_e9)) || (local_e1 <= local_e9)) ||
                     ((local_e0 <= local_e9 || (local_128[0] <= local_e8)))))) ||
                  (((local_128[1] <= local_e8 ||
                     ((local_128[3] <= local_e8 || (local_124 <= local_e8)))) ||
                    (local_123 <= local_e8)))))))))))) ||
         (((((((local_122 <= local_e8 || (local_121 <= local_e8)) || (local_120 <= local_e8)) ||
              (((local_11f <= local_e8 || (local_11e <= local_e8)) ||
                ((local_11d <= local_e8 || ((local_11c <= local_e8 || (local_11b <= local_e8))))))
              )) || (local_11a <= local_e8)) ||
            ((((local_119 <= local_e8 || (local_118 <= local_e8)) || (local_117 <= local_e8)) ||
              (((local_116 <= local_e8 || (local_115 <= local_e8)) ||
                (((local_114 <= local_e8 || ((local_113 <= local_e8 || (local_112 <= local_e8))))
                  || (local_111 <= local_e8)))))))) ||
           ((((((local_110 <= local_e8 || (local_10f <= local_e8)) || (local_10e <= local_e8)) ||
               ((local_10d <= local_e8 || (local_10c <= local_e8)))) || (local_10b <= local_e8))
             || ((((local_10a <= local_e8 || (local_109 <= local_e8)) ||
                   ((local_108 <= local_e8 ||
                     (((local_107 <= local_e8 || (local_106 <= local_e8)) || (local_104 <= local_e8)
                       ))))) || ((local_103 <= local_e8 || (local_102 <= local_e8)))))))))))))))) ||
(((((((((local_101 <= local_e8 ||
         (((local_100 <= local_e8 || (local_fe <= local_e8)) ||
           ((local_fd <= local_e8 ||
             (((local_fc <= local_e8 || (local_fb <= local_e8)) || (local_f9 <= local_e8))))))))
        || (((local_f8 <= local_e8 || (local_f7 <= local_e8)) || (local_f6 <= local_e8)))) ||
       ((((((((local_f5 <= local_e8 || (local_f4 <= local_e8)) ||
              ((local_f3 <= local_e8 ||
                ((((local_f2 <= local_e8 || (local_f1 <= local_e8)) || (local_ef <= local_e8)) ||
                  ((local_ee <= local_e8 || (local_ed <= local_e8)))))))) ||
             (local_ec <= local_e8)) || ((local_ea <= local_e8 || (local_e9 <= local_e8)))) ||
           ((local_e7 <= local_e8 ||
             (((local_e5 <= local_e8 || (local_e4 <= local_e8)) || (local_e3 <= local_e8)))))) ||
          (((local_e2 <= local_e8 || (local_e1 <= local_e8)) || (local_e0 <= local_e8)))) ||
         ((local_e7 <= local_128[0] || (local_e7 <= local_128[1])))))) ||
      (((((local_e7 <= local_128[2] ||
           (((local_e7 <= local_128[3] || (local_124 <= local_e7)) || (local_123 <= local_e7))))
          || ((local_e7 <= local_122 || (local_e7 <= local_121)))) ||
         (((local_120 <= local_e7 ||
            (((local_11f <= local_e7 || (local_e7 <= local_11e)) ||
              ((local_e7 <= local_11d ||
                ((((local_e7 <= local_11c || (local_e7 <= local_11b)) || (local_11a <= local_e7))
                  || ((local_119 <= local_e7 || (local_118 <= local_e7)))))))))) ||
           (local_e7 <= local_116)))) ||
        ((((((((local_115 <= local_e7 || (local_114 <= local_e7)) ||
               (((((local_e7 <= local_113 ||
                    (((local_112 <= local_e7 || (local_e7 <= local_111)) ||
                      (local_110 <= local_e7)))) ||
                   (((local_e7 <= local_10f || (local_e7 <= local_10e)) || (local_10d <= local_e7)
                     ))) || ((local_10c <= local_e7 || (local_e7 <= local_10b)))) ||
                 ((local_10a <= local_e7 ||
                   (((local_109 <= local_e7 || (local_e7 <= local_108)) || (local_e7 <= local_107))
                   )))))) || ((local_e7 <= local_106 || (local_e7 <= local_105)))) ||
             ((((local_104 <= local_e7 ||
                 ((((local_103 <= local_e7 || (local_e7 <= local_102)) ||
                    ((local_101 <= local_e7 ||
                      ((((((local_e7 <= local_100 || (local_e7 <= local_ff)) ||
                           (local_e7 <= local_fd)) ||
                          ((local_e7 <= local_fc || (local_e7 <= local_fb)))) ||
                         (local_e7 <= local_fa)) ||
                        ((local_f9 <= local_e7 || (local_e7 <= local_f7)))))))) ||
                   (local_e7 <= local_f6)))) ||
                ((((local_e7 <= local_f5 || (local_f4 <= local_e7)) || (local_f3 <= local_e7)) ||
                  ((local_f2 <= local_e7 || (local_f1 <= local_e7)))))) ||
               (((local_e7 <= local_f0 || ((local_ef <= local_e7 || (local_ee <= local_e7)))) ||
                 (local_ed <= local_e7)))))) ||
            (((local_e7 <= local_ec || (local_e7 <= local_eb)) || (local_ea <= local_e7)))) ||
           ((((local_e7 <= local_e9 || (local_e7 <= local_e8)) ||
              ((local_e7 <= local_e6 || ((local_e7 <= local_e5 || (local_e4 <= local_e7)))))) ||
             ((local_e3 <= local_e7 ||
               (((((local_e7 <= local_e2 || (local_e1 <= local_e7)) || (local_e0 <= local_e7)) ||
                  ((local_128[0] <= local_e6 || (local_128[1] <= local_e6)))) ||
                 ((local_128[3] <= local_e6 || ((local_124 <= local_e6 || (local_123 <= local_e6))))
                 )))))))) ||
          ((local_122 <= local_e6 ||
            (((local_121 <= local_e6 || (local_120 <= local_e6)) || (local_11f <= local_e6))))))))
      )) || ((((((local_11e <= local_e6 || (local_11d <= local_e6)) ||
                 ((local_11c <= local_e6 || ((local_11b <= local_e6 || (local_11a <= local_e6)))
                   ))) || (local_119 <= local_e6)) ||
               ((((((local_118 <= local_e6 || (local_117 <= local_e6)) ||
                    (local_116 <= local_e6)) ||
                   (((local_115 <= local_e6 || (local_114 <= local_e6)) ||
                     ((local_113 <= local_e6 ||
                       ((local_112 <= local_e6 || (local_111 <= local_e6)))))))) ||
                  ((local_110 <= local_e6 ||
                    ((((local_10f <= local_e6 || (local_10e <= local_e6)) ||
                       (local_10d <= local_e6)) ||
                      ((local_10c <= local_e6 || (local_10b <= local_e6)))))))) ||
                 ((local_10a <= local_e6 || ((local_109 <= local_e6 || (local_108 <= local_e6))))
                 )))) || ((local_107 <= local_e6 ||
                           ((((local_106 <= local_e6 || (local_104 <= local_e6)) ||
                              (local_103 <= local_e6)) ||
                             ((local_102 <= local_e6 || (local_101 <= local_e6)))))))))) ||
    ((((local_100 <= local_e6 || ((local_fe <= local_e6 || (local_fd <= local_e6)))) ||
       (local_fc <= local_e6)) ||
      ((((((local_fb <= local_e6 || (local_f9 <= local_e6)) || (local_f8 <= local_e6)) ||
          (((local_f7 <= local_e6 || (local_f6 <= local_e6)) ||
            ((local_f5 <= local_e6 || ((local_f4 <= local_e6 || (local_f3 <= local_e6)))))))) ||
         (local_f2 <= local_e6)) ||
        ((((((local_f1 <= local_e6 || (local_ef <= local_e6)) || (local_ee <= local_e6)) ||
            ((local_ed <= local_e6 || (local_ec <= local_e6)))) || (local_ea <= local_e6)) ||
          ((local_e9 <= local_e6 || (local_e7 <= local_e6)))))))))) ||
   (((((((local_e5 <= local_e6 ||
          (((local_e4 <= local_e6 || (local_e3 <= local_e6)) || (local_e2 <= local_e6)))) ||
         (((local_e1 <= local_e6 || (local_e0 <= local_e6)) || (local_e5 <= local_128[0])))) ||
        (((local_e5 <= local_128[2] || (local_e5 <= local_128[3])) ||
          ((local_124 <= local_e5 ||
            (((local_123 <= local_e5 || (local_e5 <= local_122)) || (local_e5 <= local_121))))))))
       || ((((local_120 <= local_e5 || (local_11f <= local_e5)) ||
             (((local_e5 <= local_11e ||
                ((((local_e5 <= local_11d || (local_e5 <= local_11c)) ||
                   ((local_e5 <= local_11b ||
                     ((((local_11a <= local_e5 || (local_119 <= local_e5)) ||
                        (local_118 <= local_e5)) ||
                       ((local_117 <= local_e5 || (local_e5 <= local_116)))))))) ||
                  (local_115 <= local_e5)))) ||
               (((local_114 <= local_e5 || (local_e5 <= local_113)) ||
                 ((((local_112 <= local_e5 ||
                     (((local_111 <= local_e5 || (local_110 <= local_e5)) || (local_e5 <= local_10f)
                       ))) || (((local_e5 <= local_10e || (local_10d <= local_e5)) ||
                                (local_10c <= local_e5)))) ||
                   ((local_e5 <= local_10b || (local_10a <= local_e5)))))))))) ||
            (((local_109 <= local_e5 ||
               (((local_e5 <= local_108 || (local_e5 <= local_107)) || (local_e5 <= local_105))))
              || (((local_104 <= local_e5 || (local_103 <= local_e5)) || (local_e5 <= local_102)))
              ))))) ||
      (((((((local_101 <= local_e5 || (local_e5 <= local_100)) ||
            ((local_e5 <= local_ff ||
              ((((local_fe <= local_e5 || (local_e5 <= local_fd)) || (local_e5 <= local_fb)) ||
                ((local_e5 <= local_fa || (local_f9 <= local_e5)))))))) ||
           ((local_f8 <= local_e5 || ((local_e5 <= local_f7 || (local_e5 <= local_f6)))))) ||
          (((local_e5 <= local_f5 ||
             (((local_f4 <= local_e5 || (local_f3 <= local_e5)) || (local_f2 <= local_e5)))) ||
            (((local_f1 <= local_e5 || (local_e5 <= local_f0)) || (local_ef <= local_e5)))))) ||
         (((((local_ee <= local_e5 || (local_ed <= local_e5)) ||
             ((local_ec <= local_e5 ||
               (((local_e5 <= local_eb || (local_ea <= local_e5)) || (local_e5 <= local_e9)))))) ||
            ((local_e5 <= local_e8 || (local_e7 <= local_e5)))) ||
           ((local_e5 <= local_e6 ||
             (((local_e4 <= local_e5 || (local_e3 <= local_e5)) ||
               ((local_e5 <= local_e2 ||
                 (((((local_e1 <= local_e5 || (local_e0 <= local_e5)) || (local_e4 <= local_128[0]))
                    || ((local_e4 <= local_128[1] || (local_e4 <= local_128[2])))) ||
                   (local_e4 <= local_128[3])))))))))))) ||
        ((((local_124 <= local_e4 || (local_e4 <= local_123)) ||
           ((local_e4 <= local_122 ||
             (((local_e4 <= local_121 || (local_e4 <= local_120)) || (local_e4 <= local_11f))))))
          || ((((((((local_e4 <= local_11e || (local_e4 <= local_11d)) ||
                    ((local_e4 <= local_11c || ((local_e4 <= local_11b || (local_e4 <= local_11a)))
                      ))) || (local_e4 <= local_119)) ||
                  ((((local_e4 <= local_118 || (local_e4 <= local_117)) || (local_e4 <= local_116))
                    || ((local_e4 <= local_115 || (local_e4 <= local_114)))))) ||
                 (((((local_e4 <= local_113 || ((local_e4 <= local_112 || (local_e4 <= local_111)))
                      ) || (local_e4 <= local_110)) ||
                    (((((local_e4 <= local_10f || (local_e4 <= local_10e)) ||
                        (local_e4 <= local_10d)) ||
                       ((local_e4 <= local_10c || (local_e4 <= local_10b)))) ||
                      ((local_e4 <= local_10a || ((local_e4 <= local_109 || (local_e4 <= local_108)))
                        ))))) || (local_e4 <= local_107)))) ||
                ((((local_e4 <= local_106 || (local_e4 <= local_105)) || (local_104 <= local_e4))
                  || ((((local_e4 <= local_102 || (local_e4 <= local_101)) ||
                        ((local_e4 <= local_100 || ((local_e4 <= local_ff || (local_e4 <= local_fe)))
                          ))) || ((local_e4 <= local_fd ||
                                   (((local_e4 <= local_fc || (local_e4 <= local_fb)) ||
                                     (local_e4 <= local_fa)))))))))) ||
               ((((local_e4 <= local_f9 || (local_e4 <= local_f8)) ||
                  (((((local_e4 <= local_f7 || ((local_e4 <= local_f6 || (local_e4 <= local_f5))))
                      || (local_e4 <= local_f4)) ||
                     ((((((local_e4 <= local_f3 || (local_e4 <= local_f2)) || (local_e4 <= local_f1))
                         || ((local_e4 <= local_f0 || (local_e4 <= local_ef)))) ||
                        ((local_e4 <= local_ee || ((local_e4 <= local_ed || (local_e4 <= local_ec)))))
                        ) || ((local_e4 <= local_eb ||
                               ((((local_e4 <= local_ea || (local_e4 <= local_e9)) ||
                                  (local_e4 <= local_e8)) ||
                                 (((local_e4 <= local_e7 || (local_e4 <= local_e6)) ||
                                   ((local_e4 <= local_e5 ||
                                     ((local_e4 <= local_e3 || (local_e4 <= local_e2)))))))))))))) ||
                    (local_e4 <= local_e1)))) ||
                 (((local_e0 <= local_e4 || (local_e3 <= local_128[0])) ||
                   (local_e3 <= local_128[1])))))))))))) ||
     ((((((local_e3 <= local_128[2] || (local_e3 <= local_128[3])) ||
          ((((local_124 <= local_e3 || ((local_123 <= local_e3 || (local_e3 <= local_122)))) ||
             (local_e3 <= local_121)) ||
            ((((((local_e3 <= local_120 || (local_11f <= local_e3)) || (local_e3 <= local_11e)) ||
                ((local_e3 <= local_11d || (local_e3 <= local_11c)))) || (local_e3 <= local_11b))
              || ((local_e3 <= local_11a || (local_e3 <= local_119)))))))) ||
         (((local_118 <= local_e3 ||
            (((local_e3 <= local_117 || (local_e3 <= local_116)) || (local_e3 <= local_115)))) ||
           (((local_114 <= local_e3 || (local_e3 <= local_113)) || (local_112 <= local_e3)))))) ||
        ((local_e3 <= local_111 || (local_e3 <= local_110)))) ||
       ((((local_e3 <= local_10f ||
           (((local_e3 <= local_10e || (local_e3 <= local_10d)) || (local_10c <= local_e3)))) ||
          (((((local_e3 <= local_10b || (local_e3 <= local_10a)) ||
              ((local_109 <= local_e3 ||
                ((((local_e3 <= local_108 || (local_e3 <= local_107)) ||
                   ((local_e3 <= local_106 ||
                     ((((local_e3 <= local_105 || (local_104 <= local_e3)) || (local_103 <= local_e3))
                       || ((local_e3 <= local_102 || (local_e3 <= local_101)))))))) ||
                  (local_e3 <= local_100)))))) || ((local_e3 <= local_ff || (local_e3 <= local_fe))))
            || (((local_e3 <= local_fd ||
                  (((local_e3 <= local_fc || (local_e3 <= local_fb)) || (local_e3 <= local_fa)))) ||
                 (((local_e3 <= local_f9 || (local_e3 <= local_f8)) || (local_e3 <= local_f7))))))))
         || ((((local_e3 <= local_f6 || (local_e3 <= local_f5)) ||
               ((local_e3 <= local_f4 ||
                 (((local_f3 <= local_e3 || (local_f2 <= local_e3)) || (local_e3 <= local_f1))))))
              || (((local_e3 <= local_f0 || (local_ef <= local_e3)) || (local_ee <= local_e3)))))))
       ))))) ||
(((((((((local_e3 <= local_ed || (local_e3 <= local_ec)) ||
        ((local_e3 <= local_eb ||
          ((((local_ea <= local_e3 || (local_e3 <= local_e9)) || (local_e3 <= local_e8)) ||
            ((local_e3 <= local_e7 || (local_e3 <= local_e6)))))))) ||
       ((local_e3 <= local_e5 || ((local_e4 <= local_e3 || (local_e3 <= local_e2)))))) ||
      ((((local_e0 <= local_e3 ||
          (((local_e2 <= local_128[0] || (local_128[1] <= local_e2)) ||
            (local_e2 <= local_128[2])))) ||
         (((local_e2 <= local_128[3] || (local_124 <= local_e2)) || (local_123 <= local_e2))))
        || (((local_e2 <= local_122 || (local_e2 <= local_121)) ||
             ((local_120 <= local_e2 ||
               (((local_11f <= local_e2 || (local_e2 <= local_11d)) || (local_11c <= local_e2))))
             )))))) || ((local_e2 <= local_11b || (local_11a <= local_e2)))) ||
    ((local_119 <= local_e2 ||
      (((local_118 <= local_e2 || (local_117 <= local_e2)) ||
        ((local_e2 <= local_116 ||
          (((((local_115 <= local_e2 || (local_114 <= local_e2)) || (local_113 <= local_e2)) ||
             ((local_112 <= local_e2 || (local_111 <= local_e2)))) || (local_110 <= local_e2))))))
      )))) || ((((((local_e2 <= local_10f || (local_e2 <= local_10e)) ||
                   ((local_10d <= local_e2 ||
                     (((((local_10c <= local_e2 || (local_e2 <= local_10b)) ||
                         (local_10a <= local_e2)) ||
                        (((local_109 <= local_e2 || (local_e2 <= local_108)) ||
                          ((local_e2 <= local_107 ||
                            ((local_106 <= local_e2 || (local_e2 <= local_105)))))))) ||
                       (local_104 <= local_e2)))))) ||
                  ((((local_103 <= local_e2 || (local_e2 <= local_102)) ||
                     (local_101 <= local_e2)) ||
                    ((local_e2 <= local_100 || (local_e2 <= local_ff)))))) ||
                 (((((((((local_fe <= local_e2 ||
                          ((local_e2 <= local_fd || (local_fc <= local_e2)))) ||
                         (local_e2 <= local_fb)) ||
                        ((((((local_e2 <= local_fa || (local_f9 <= local_e2)) ||
                             (local_f8 <= local_e2)) ||
                            ((local_e2 <= local_f7 || (local_e2 <= local_f6)))) ||
                           ((local_e2 <= local_f5 ||
                             ((local_f4 <= local_e2 || (local_f3 <= local_e2)))))) ||
                          (local_f2 <= local_e2)))) ||
                       ((((local_f1 <= local_e2 || (local_e2 <= local_f0)) ||
                          (local_ef <= local_e2)) ||
                         (((local_ee <= local_e2 || (local_ed <= local_e2)) ||
                           ((local_ec <= local_e2 ||
                             ((local_e2 <= local_eb || (local_ea <= local_e2)))))))))) ||
                      (local_e2 <= local_e9)) ||
                     ((((local_e2 <= local_e8 || (local_e7 <= local_e2)) ||
                        (local_e2 <= local_e6)) ||
                       (((local_e5 <= local_e2 || (local_e4 <= local_e2)) ||
                         ((local_e3 <= local_e2 ||
                           ((local_e1 <= local_e2 || (local_e0 <= local_e2)))))))))) ||
                    (((local_e1 <= local_128[0] ||
                       ((((local_e1 <= local_128[1] || (local_e1 <= local_128[2])) ||
                          (local_e1 <= local_128[3])) ||
                         ((local_124 <= local_e1 || (local_123 <= local_e1)))))) ||
                      (((local_e1 <= local_122 ||
                         ((local_e1 <= local_121 || (local_e1 <= local_120)))) ||
                        (local_11f <= local_e1)))))) ||
                   ((((((((local_e1 <= local_11e || (local_e1 <= local_11d)) ||
                          (local_e1 <= local_11c)) ||
                         (((local_e1 <= local_11b || (local_e1 <= local_11a)) ||
                           ((local_e1 <= local_119 ||
                             ((local_118 <= local_e1 || (local_e1 <= local_117)))))))) ||
                        ((local_e1 <= local_116 ||
                          (((local_e1 <= local_115 || (local_114 <= local_e1)) ||
                            (local_e1 <= local_113)))))) ||
                       ((local_112 <= local_e1 || (local_e1 <= local_111)))) ||
                      (((((local_e1 <= local_110 ||
                           ((local_e1 <= local_10f || (local_e1 <= local_10e)))) ||
                          (local_e1 <= local_10d)) ||
                         ((((((local_10c <= local_e1 || (local_e1 <= local_10b)) ||
                              (local_e1 <= local_10a)) ||
                             ((local_109 <= local_e1 || (local_e1 <= local_108)))) ||
                            (local_e1 <= local_107)) ||
                           ((((local_e1 <= local_106 || (local_e1 <= local_105)) ||
                              ((local_104 <= local_e1 ||
                                (((local_103 <= local_e1 || (local_e1 <= local_102)) ||
                                  (local_e1 <= local_101)))))) ||
                             ((local_e1 <= local_100 || (local_e1 <= local_ff)))))))) ||
                        ((local_e1 <= local_fe ||
                          (((((local_e1 <= local_fd || (local_e1 <= local_fc)) ||
                              ((local_e1 <= local_fb ||
                                (((local_e1 <= local_fa || (local_e1 <= local_f9)) ||
                                  (local_e1 <= local_f8)))))) ||
                             (((local_e1 <= local_f7 || (local_e1 <= local_f6)) ||
                               ((local_e1 <= local_f5 ||
                                 (((local_e1 <= local_f4 || (local_f3 <= local_e1)) ||
                                   ((local_f2 <= local_e1 ||
                                     ((((local_e1 <= local_f1 || (local_e1 <= local_f0)) ||
                                        (local_ef <= local_e1)) ||
                                       ((local_ee <= local_e1 || (local_e1 <= local_ed)))))))))))))) ||
                            (local_e1 <= local_ec)))))))) ||
                     (((local_e1 <= local_eb || (local_ea <= local_e1)) ||
                       ((local_e1 <= local_e9 ||
                         (((local_e1 <= local_e8 || (local_e1 <= local_e7)) ||
                           (local_e1 <= local_e6)))))))))))) ||
                (((((((local_e1 <= local_e5 || (local_e4 <= local_e1)) || (local_e1 <= local_e2)
                      ) || ((local_e0 <= local_e1 || (local_e0 <= local_128[0])))) ||
                    ((local_e0 <= local_128[1] ||
                      (((local_e0 <= local_128[2] || (local_e0 <= local_128[3])) ||
                        (local_e0 <= local_124)))))) ||
                   (((((local_e0 <= local_123 || (local_e0 <= local_122)) ||
                       ((local_e0 <= local_121 ||
                         (((local_e0 <= local_120 || (local_e0 <= local_11f)) ||
                           ((local_e0 <= local_11e ||
                             ((((local_e0 <= local_11d || (local_e0 <= local_11c)) ||
                                (local_e0 <= local_11b)) ||
                               ((local_e0 <= local_11a || (local_e0 <= local_119)))))))))))) ||
                      (local_e0 <= local_118)) ||
                     ((local_e0 <= local_117 || (local_e0 <= local_116)))))) ||
                  ((((local_e0 <= local_115 ||
                      (((local_e0 <= local_114 || (local_e0 <= local_113)) ||
                        (local_e0 <= local_112)))) ||
                     (((local_e0 <= local_111 || (local_e0 <= local_110)) ||
                       (local_e0 <= local_10f)))) ||
                    ((local_e0 <= local_10e || (local_e0 <= local_10d)))))))))) ||
  ((((local_e0 <= local_10c ||
      (((local_e0 <= local_10b || (local_e0 <= local_10a)) || (local_e0 <= local_109)))) ||
     (((local_e0 <= local_108 || (local_e0 <= local_107)) ||
       ((local_e0 <= local_106 ||
         (((local_e0 <= local_105 || (local_e0 <= local_104)) ||
           ((local_e0 <= local_103 ||
             (((((((local_e0 <= local_102 || (local_e0 <= local_101)) || (local_e0 <= local_100))
                  || ((local_e0 <= local_ff || (local_e0 <= local_fe)))) || (local_e0 <= local_fd))
                || ((local_e0 <= local_fc || (local_e0 <= local_fb)))) || (local_e0 <= local_fa)))))
           ))))))) ||
    ((((((local_e0 <= local_f9 || (local_e0 <= local_f8)) || (local_e0 <= local_f7)) ||
        ((local_e0 <= local_f6 || (local_e0 <= local_f5)))) || (local_e0 <= local_f4)) ||
      (((((((local_e0 <= local_f3 || (local_e0 <= local_f2)) ||
            ((local_e0 <= local_f1 ||
              (((local_e0 <= local_f0 || (local_e0 <= local_ef)) || (local_e0 <= local_ee)))))) ||
           ((local_e0 <= local_ed || (local_e0 <= local_ec)))) || (local_e0 <= local_eb)) ||
         (((local_e0 <= local_ea || (local_e0 <= local_e9)) ||
           ((local_e0 <= local_e8 ||
             ((((local_e0 <= local_e7 || (local_e0 <= local_e6)) || (local_e0 <= local_e5)) ||
               ((local_e0 <= local_e4 || (local_e0 <= local_e3)))))))))) ||
        ((local_e0 <= local_e2 || (local_e0 <= local_e1))))))))))))))))""".replace("<=",">")
tosolve = tosolve.replace("local_128[0]","local_128")
tosolve = tosolve.replace("local_128[1]","local_127")
tosolve = tosolve.replace("local_128[2]","local_126")
tosolve = tosolve.replace("local_128[3]","local_125")
s = Solver()
for num in range(0x128,0xe0 - 1,-1):
    varname = "local_" + hex(num)[2:]
    exec(f"{varname} = Int('{varname}')")
    #exec(f"s.add(96 < {varname} < 127 or 35 < {varname} < 67)")
    exec(f"temp1 = Or(96 < {varname},{varname} < 127)")
    exec(f"temp2 = Or(48 <= {varname},{varname} <= 57)")
    temp3 = Or(temp1,temp2)
    s.add(temp3)
tosolve = list(map(str.strip,tosolve.replace("(","").replace(")","").split("||")))[1:]
for condition in tosolve:
    exec(f"s.add({condition})")
print(s.check())
final = s.model()
flag = ""
print(final)
for num in range(0x128,0xe0 - 1,-1):
    varname = "local_" + hex(num)[2:]
    flag += chr(eval(f"final[{varname}].as_long()"))
print(flag)
