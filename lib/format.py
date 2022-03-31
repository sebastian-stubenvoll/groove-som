def meshData(matrix):
    x, y = matrix.shape
    mesh = ''
    for i in range (0,x):
        for j in range(0,y):
            mesh += f'{i}\t{j}\t{matrix[i,j]}\n'
        mesh += '\n'
    return mesh


def lableTable(songs):
    tbl = '\\begin{table}[h]\n'
    tbl += '    \\begin{center}\n'
    tbl += '        \\being{tabular}{lccc}\n'
    tbl += '            \\toprule\n'
    row = 'id & Performer & Title & Duration [s]'
    tbl += f'                {row}\n'
    for i,s in enumerate(songs):
        row = f'{i+1} & {s.performer} & {s.title} & {s.length}'
        tbl += f'                {row}\n'

    tbl += '            \\buttomrule\n'
    tbl += '        \\end{tabular}\n'
    tbl += '    \\end{center}\n'
    tbl += '\\end{table}\n'
    return tbl

