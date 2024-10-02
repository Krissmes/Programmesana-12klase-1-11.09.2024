def lielakasSkaitlis(skaitlis1, skaitlis2, skaitlis3):
    if skaitlis1 > skaitlis2 and skaitlis1 > skaitlis3:
        print(skaitlis1, "ir viss lieklākais")
    if skaitlis2 > skaitlis3 and skaitlis2 > skaitlis1:
        print(skaitlis2, "ir viss lieklākais")
    if skaitlis3 > skaitlis2 and skaitlis3 > skaitlis1:
        print(skaitlis3, "ir viss lieklākais")
lielakasSkaitlis(1,2,3)