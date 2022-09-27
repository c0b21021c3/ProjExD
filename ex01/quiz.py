import random
quiz_list = ["令和元年は西暦何年？",
"教科書販売は東京工業大学八王子キャンパスの「○○棟」にある。「○○」を埋めよ",
"「左ける」これは何と読むか"]

quiz_ans_list = [("2019年", 2019,"２０１９","にせんじゅうきゅうねん","二千十九年"),
("ほんぶ","本部"),
("たすける","タスケル")]

print("問題")
qn = random.randint(0,2)
print(quiz_list[qn])

anser = input("お答えください(変な空白を入れないでね。お願いします): ")

if anser in quiz_ans_list[qn]:
    print("正解")
else:
    print("なんか……ごめんね")