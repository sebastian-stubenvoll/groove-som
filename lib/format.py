def meshData(matrix):
    x, y = matrix.shape
    mesh = ''
    for i in range (0,x):
        for j in range(0,y):
            mesh += f'{i}\t{j}\t{matrix[i,j]}\n'
        mesh += '\n'
    return mesh


def lableTable(songs):
    fmt = lambda s: s.replace('$', '\\$').replace('&', '\\&')
    tbl = '\\begin{tabular}{lccc}\n'
    tbl += '    \\toprule\n'
    row = 'id & Performer & Title & Duration [s]'
    tbl += f'       {row}\\\\ \n'
    tbl += '    \\midrule\n'
    for i,s in enumerate(songs):
        row = f'{i+1} & {fmt(s.performer)} & {fmt(s.title)} & {s.length}'
        tbl += f'       {row}\\\\ \n'

    tbl += '    \\bottomrule\n'
    tbl += '\\end{tabular}\n'
    return tbl

