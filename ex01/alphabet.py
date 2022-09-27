import random
import time
tn = 10#大正文字列数
ln = 2#欠損文字列数
f = 6#最大挑戦回数

def gentxt():#リストで対象文字列を生成
    global tn
    al = "abcdefghijklmnopqrstuvwxyz".upper()
    txt = random.sample(al,tn) 
    return txt

def rtxt(txt):
    """リストの要素を欠損文字列分だけ削除し、削除後にシャッフルをする
    削除・シャッフルしたリストと、消した文字をタプルで返す
    """
    global ln
    t = txt.copy()#リストの大本を破壊してはいけない！！
    r = random.sample(t,ln)
    for i in r:
        t.remove(i)
    random.shuffle(t)
    return (t, r)

start = time.time()
times = 1
while times <= f:
    times += 1
    txt = gentxt()
    rmtxt , rmw = rtxt(txt)
    ts = [" ".join(i) for i in [txt,rmtxt,rmw]]
    print(f"対象文字:\n{ts[0]}\n表示文字:\n{ts[1]}\n")
    ans1 = int(input("欠損文字はいくつあるでしょうか？: "))
    if ans1 == ln:
        print("正解です")
        ans2 = []
        for i in range(1,ln+1):
            ans2.append(input(f"{i}つ目の文字を入力してください: "))
        if (ans2 == rmw) or (ans2[::-1] == rmw):
            print("正解です")
            times = f+1
            break
        else:print("不正解です")

    else: print("不正解です")

finish = time.time() - start
print(f"経過時間: {round(finish)}秒")