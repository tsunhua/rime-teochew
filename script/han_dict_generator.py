#!/usr/bin/python
# -*- coding: UTF-8 -*-
#

def transfer():
    source = open('../source/dieziu.dict.yaml', 'r')
    dest = open('../teochew.han.dict.yaml', 'w')
    cor = open('../source/correction.txt', 'r')
    dest.writelines('''# Rime dictionary
# encoding:	utf-8
#
# Teochew Han 潮州話漢字
#
---
name:	teochew.han
version:	"0.2"
sort:	by_weight
use_preset_vocabulary:	false
...
''')
    corretion = {}
    while line := cor.readline():
        ws = line.split('\t')
        if len(ws) <= 1:
            continue
        corretion[ws[0].strip()] = ws[1].strip()

    while line := source.readline():
        ws = line.split('\t')
        if len(ws) <= 1:
            continue
        yin = ''
        if ws[0].strip() in corretion:
            yin = corretion[ws[0].strip()]
        else:
            yin = to_bl(ws[1].strip())
        dest.write('%s\t%s\n' % (ws[0].strip(), yin))
    dest.close()
    source.close()
    cor.close()
    pass

def to_bl(yin):
    # -n=>-nn
    if yin[len(yin) - 2] == 'n':
        yin = yin[0:len(yin) - 2] + 'nn' + yin[len(yin) - 1]
    # remove 1,4
    if yin.endswith('1') or yin.endswith('4'):
        yin = yin[0:len(yin) - 1]
    # v=>ur
    yin = yin.replace('v', 'ur')
    # ieng => ien
    yin = yin.replace('ieng', 'ien')
    # iek => iet
    yin = yin.replace('iek', 'iet')
    # ueng => uen
    yin = yin.replace('ueng', 'uen')
    # uek => uet
    yin = yin.replace('uek', 'uet')
    # ung => un
    yin = yin.replace('ung', 'un')
    # uk => ut
    yin = yin.replace('uk','ut')
    # urng => urn
    yin = yin.replace('urng', 'urn')
    # urk => urt
    yin = yin.replace('urk', 'urt')
    # ing => in
    yin = yin.replace('ing', 'in')
    # ik => it
    yin = yin.replace('ik', 'it')
    # p=>ph, t=>th, k=>kh
    if yin.startswith("p") or yin.startswith('t') or yin.startswith('k'):
        yin = yin[0:1] + 'h' + yin[1:len(yin)]
        return yin
    # b=>p, d=>t, g=>k
    if yin.startswith('b') and not yin.startswith('bh'):
        yin = 'p' + yin[1:len(yin)]
        return yin
    if yin.startswith('d'):
        yin = 't' + yin[1:len(yin)]
        return yin
    if yin.startswith('g') and not yin.startswith('gh'):
        yin = 'k' + yin[1:len(yin)]
        return yin
    # bh=>b, gh=>g
    if yin.startswith("bh") or yin.startswith('gh'):
        yin = yin[0:1] + yin[2:len(yin)]
        return yin
    # z=>ts/ch, c=>tsh/chh
    if yin.startswith("z"):
        # ch,chh,j 只用於e，和i前面
        if yin[1:2] in ['e', 'i']:
            yin = 'ch' + yin[1:len(yin)]
        else:
            yin = 'ts' + yin[1:len(yin)]
        return yin
    if yin.startswith('c'):
        if yin[1:2] in ['e', 'i']:
            yin = 'chh' + yin[1:len(yin)]
        else:
            yin = 'tsh' + yin[1:len(yin)]
        return yin
    # r=>j/z
    if yin.startswith('r'):
        if yin[1:2] in ['e', 'i']:
            yin = 'j' + yin[1:len(yin)]
        else:
            yin = 'z' + yin[1:len(yin)]
        return yin
    return yin


if __name__ == "__main__":
    transfer()
    pass