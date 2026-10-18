# def calculate_love_score(name1,name2):
#     name1 = name1+name2
#     true = 0
#     love = 0
#     for letters in name1 :
#           if letters == "t" or letters == "r" or letters == "u" or letters == "e" :
#             true += 1
#     for letters in name1 :
#           if letters == "l" or letters == "o" or letters == "v" or letters == "e" :
#             love += 1
#     print(true)
#     print(love)
#     calculate = int((str(true)+str(love)))
#     if calculate > 100 :
#         calculate = 100
#     print(f"{calculate} %")
# # calculate_love_score("Kanye West", "Kim Kardashian")
# name1 = input("enter 1st name ")
# name2 = input("enter 2nd name ")
# calculate_love_score(name1,name2)


def calculate_love_score(name1,name2):
    name1 = name1+name2
    true = 0
    love = 0
    for letters in name1 :
          for chars in "true":
            if chars == letters :
                true += 1
          for chars in "love":
            if chars == letters :
                love += 1
    # print(true)
    # print(love)
    calculate = int((str(true)+str(love)))
    if calculate > 100 :
        calculate = 100
    print(f"{calculate} %")
name1 = input("enter 1st name ")
name2 = input("enter 2nd name ")
calculate_love_score(name1,name2)