print("ㅎㅇ")
print("입력은 한 글자씩치고 엔터 눌러야 댐")
print("플랫,샾은 입력하면 안 댐 귀찮아서 그거 안 넣어놓음")
print("현재 변환 가능한 범위: 낮은 미~높은 솔")
print("높은, 낮은 음 입력 할 때 띄어쓰기 꼭 넣어야 댐")
print('"그만할랭"을 입력해서 종료할 수 있음ㅇㅇ')




paper=["","","","","",""]
name=["낮은 미","낮은 파","낮은 솔","낮은 라","낮은 시","도","레","미","파","솔","라","시","높은 도","높은 레", "높은 미","높은 파","높은 솔"]
kirm=[(6,0),(6,1),(6,3),(5,0),(5,2),(5,3),(4,0),(4,2),(4,3),(3,0),(3,2),(2,0),(2,1),(2,3),(1,0),(1,1),(1,3)]

while True:
    banana=open("예아.txt","w",encoding="UTF-8")
    keke=input("에..음을 입력해보세요:")
    if keke in name:
        x=name.index(keke)
        print(kirm[x])
        for aa in range(6):
            paper[aa]=paper[aa]+"=="
            if aa==kirm[x-1][0]:
                paper[aa]=paper[aa]+str(kirm[x][1])
            else:
                paper[aa]=paper[aa]+"="
        print("입력했어요")
    elif keke=="그만할랭":
        print(paper)
        for bb in range(6):
            banana.write(paper[bb])
            banana.write("\n")
        banana.close()
        break
    else:
        print("예?")
