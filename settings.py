level_map1 = [
'                                      ',
'                                CC    ',
'                                XX    ',
'  L E   R            L   E  R         ',
'  XXXXXXX            XXXXXXXX  CC     ',
'  DDDDDDDX        X            XXX    ',
'  DDDD                    C           ',
'         L    C   ER     XXX          ',
'         XXXXXXXXXXX    XDDDXXX      C',
'    P    DDDDDDDDDDDX   DDDDDDDXX    C',
'    XXXXXDDDDDDDDDDDDLERDDDDDDDDD    C',
'XXXXDDDDDDDDDDDDDDDDDXXXDDDDDDDDDXX XX']

level_map2 = [
'                               CCI              ',
'                          C    XXX              ',
'  L C   P    ER      C     X                    ',
'  XXXXXXXXXXXXX     X     X                     ',
'  DDDDDDDDDD        D     D    L ER             ',
'  DDDDDDDDDD      XXD          XXXX         CCCC',
'                              XDDDDX        CCCC',
'         L        ER      XXXXDDDDDD        XXXX',
'         XXXXXXXXXXX      DDDDDDDDDDX           ',
'    LECCRDDDDDDDDDDDX              DDX          ',
' I  XXXXXDDDDDDDDDDDDXL   E CCCCC RDDD          ',
'XXXXDDDDDDDDDDDDDDDDDDXXXXXXXXXXXXXDDD          ']

level_map3 = [
'                                        XXX  XXXXXXXXXXX',
'                    CCC  L E R                          ',
'    P                    XXXXX                    CCCCC ',
'XXXXX                             I               CCCCC ',
'DDDDDX     C              C     XXX         X      XXX  ',
'          XX         C   XXX    DDDX              XDDDX ',
'          DD        XXX                                 ',
'          DD    X                                       ',
'  CCC   XXDD    D           L E  R                      ',
'  XXXCC        XD     XX    XXXXXX                      ',
'I DDDXXL   E  RDD          XDDDDDDCC                    ',
'XXDDDDDXXXXXXXXXXXX      XXDDDDDDDXXX                   ']

level_map4 = [
'                  CCCC               ',
'  C              XXXXXXX             ',
'XXXXXX                               ',
'DDDDD                          C     ',
'                       C     XXX     ',
'  P               C    XXX   DDDX    ',
'  X      E     XXX                   ',
'         XX                          ',
'                E      E             ',
'  XXXCC        XX      XX   XXXXXX   ',
'  DDDXX        DD          XDDDDDDCC ',
'XXDDDDDXXXXXXXXDD         XDDDDDDDXXX']

level_map5 = [
'          CCC XXXXXXXXXXXL C CEC C R                            ',
'         XXXXXDDDDDDDDDDDXXXXXXXXXXX   I                        ',
'      XXXDDDDDDDD       DDDDDDDDDDDDXXXXXX              C C     ',
'       DDDD                        DDDDDDD             C   C    ',
'       DDDDL  E R            C          DD              CCC     ',
'        DDDXXXXXX      X     X      C       C                   ',
'        DD                          X       X                   ',
'         DL ER                     XD   X                       ',
'         DXXXX                                                  ',
'                                                 L  C C E C C  R',
'PL   E  R                                        XXXXXXXXXXXXXXX',
'XXXXXXXXX      XX                                 DDDDDDDDDDDDD ']


tile_size = 60
screen_width = 1200
screen_height = len(level_map1) * tile_size  # this is so the height is relative to the level map
