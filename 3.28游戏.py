import random
allList = ['ʯͷ', '����', '��']
winList = ['ʯͷ', '����'], ['����', '��'], ['��', 'ʯͷ']
chnum = 1
prompt = '''
===��ӭ�μ�ʯͷ��������Ϸ===
��ѡ��
0   ʯͷ
1   ����
2   ��
3   �Ҳ�����
=============================
'''
while True:
    chnum = input(prompt)
    if chnum not in ['0', '1', '2', '3']:
        print("��Ч��ѡ����ѡ��0/1/2/3")
        continue
    if chnum == '3':
        break
    cchoice = random.choice(allList)
    uchoice = allList[int(chnum)]
    print("��ѡ���ˣ�{}\n�����ѡ���ˣ�{}".format(uchoice,cchoice))
    if uchoice == cchoice:
        print("ƽ��")
    elif [uchoice,cchoice] in winList:
        print("��Ӯ�ˣ�����")
    else:
        print("�����ˣ�����")
print("��Ϸ������")
