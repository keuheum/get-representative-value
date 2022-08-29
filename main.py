def get_mode(list_):
    mode_dict = {}
    for i in list_:
        if i in mode_dict:
            mode_dict[i] += 1
        else:
            mode_dict[i] = 1

    mode_list = sorted(list(mode_dict.values()), reverse=True)

    if mode_list[0] == 1:
        return "최빈값이 존재하지 않음."
    else:
        mode_str = ""
        for k, v in mode_dict.items():
            if v == mode_list[0]:
                mode_str += f"{k} "
        mode_str += f"| {mode_list[0]}회"
        return mode_str

def get_median(list_):
    if len(list_)%2 == 0:#짝수
        return f"{(list_[len(list_)//2] + list_[len(list_)//2-1]) / 2}"
        
    else:#홀수
        return list_[len(list_)//2]

num_list = []

while True:
    num_input = input(": ")
    if num_input == ".":
        break
    else:
        try:
            num_input = int(num_input)
        except:
            print("숫자 아님, 무시됨.")
        else:
            num_list.append(num_input)

num_list.sort()

print(f"리스트 값     : {num_list}")
print(f"리스트 길이   : {len(num_list)}")
print(f"리스트 평균값 : {sum(num_list)/len(num_list)} | ({sum(num_list)}/{len(num_list)})")
print(f"리스트 최빈값 : {get_mode(num_list)}")
print(f"리스트 중앙값 : {get_median(num_list)}")
