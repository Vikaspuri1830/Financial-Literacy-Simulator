from tkinter import *
from tkinter import messagebox
import datetime
from tkinter import ttk
import sqlite3

heading_font = ("Arial Bold", 45)
label_font = ("Arial Light", 20)
card_btn_font = ("Arial", 18)
entry_font = ("Arial", 18)
entry_bg = "#FFFFFF"
label_fg = "#F7F7FF"
base_bg = "#006d77"
term_font = ("Arial", 30)
btn_canvas_bg = "#006d77"
fun_btn_fg = "#F8F1FF"
fun_btn_bg = "#007B86"
fun_btn_fnt = ("Verdana", 14)
checkbtn_bg = "#006d77"
checkbtn_fg = "#DAF5FF"
small_lb_font = ("Arial", 18)
heading_fg = "#F7F7FF"
btn_bg = "#FFFB87"

def exit():
    main_window()

qnum = 0
def quiz_tab():
    submitted = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    def previous():
        global qnum
        if qnum > 0:
            submitted[qnum] = int(var.get())
            qnum -= 1
            update_question()

    def next():
        global qnum
        if qnum < len(questions) - 1:
            submitted[qnum] = int(var.get())
            qnum += 1
            update_question()

    def submit():
        submitted[qnum] = int(var.get())
        flag = 1
        for a in submitted:
            if a == 0:
                flag = 2
        if flag == 1:
            answers = [3, 2, 3, 1, 3, 4, 4, 3, 3, 4]
            count = 0
            i = 0
            while i <=9:
                if submitted[i] == answers[i]:
                    count += 1
                i = i + 1

            result_canvas = Canvas(base, bg=base_bg)
            result_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

            result = Label(result_canvas, text="You have scored " + str(count) + "/10", font=heading_font, bg=base_bg, fg=label_fg)
            result.place(relx=0.3, rely=0.35)

            back_btn = Button(result_canvas, text="Back", font=card_btn_font, bg=btn_bg, command=exit)
            back_btn.place(relx=0.9, rely=0.07, relwidth=0.07, relheight=0.05)            
        
        
        else:
            messagebox.showwarning("Fail Submission", "Please attempt all the questions...")   

    def update_question():
        question_count.config(text=f"Q.{qnum + 1}/{len(questions)}")
        question.config(text=questions[qnum][1])
        var.set(None)  # Clear the selected answer
        op1.config(text=questions[qnum][2])
        op2.config(text=questions[qnum][3])
        op3.config(text=questions[qnum][4])
        op4.config(text=questions[qnum][5])

    con = sqlite3.connect("fls_db.db")
    q = "select * from quiz"
    cursor = con.cursor()
    cursor.execute(q)
    questions = cursor.fetchall()
    con.commit()
    con.close()

    quiz_canvas = Canvas(base, bg=base_bg)
    quiz_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

    category_heading = Label(quiz_canvas, text="Category : " + questions[qnum][0], font=("Times New Roman", 50), bg=base_bg, fg=heading_fg)
    category_heading.place(relx=0.33, rely=0.06)

    question_canvas = Canvas(base, bg=base_bg)
    question_canvas.place(relx=0, rely=0.21, relheight=0.8, relwidth=1)

    question_count = Label(question_canvas, text="Q.1/10", font=label_font, bg=base_bg, fg=label_fg)
    question_count.place(relx=0.9, rely=0.06)

    question = Label(question_canvas, text=questions[qnum][1], font=label_font, bg=base_bg, fg=label_fg)
    question.place(relx=0.2, rely=0.1)

    var = StringVar(question_canvas)

    op1 = Radiobutton(question_canvas, text=questions[qnum][2], font=label_font, variable=var, value="1", bg=checkbtn_bg, fg=checkbtn_fg, selectcolor="#0084A1")

    op1.place(relx=0.21, rely=0.17)
    # male.select()

    op2 = Radiobutton(question_canvas, text=questions[qnum][3], font=label_font, variable=var, value="2", bg=checkbtn_bg, fg=checkbtn_fg, selectcolor="#0084A1")
    op2.place(relx=0.21, rely=0.24)

    op3 = Radiobutton(question_canvas, text=questions[qnum][4], font=label_font, variable=var, value="3", bg=checkbtn_bg, fg=checkbtn_fg, selectcolor="#0084A1")
    op3.place(relx=0.21, rely=0.31)

    op4 = Radiobutton(question_canvas, text=questions[qnum][5], font=label_font, variable=var, value="4", bg=checkbtn_bg, fg=checkbtn_fg, selectcolor="#0084A1")
    op4.place(relx=0.21, rely=0.38)

    previous_btn = Button(question_canvas, text="Previous", font=card_btn_font, bg=btn_bg, command=previous)
    previous_btn.place(relx=0.24, rely=0.53, relwidth=0.1, relheight=0.1)

    next_btn = Button(question_canvas, text="Next", font=card_btn_font, bg=btn_bg, command=next)
    next_btn.place(relx=0.48, rely=0.53, relwidth=0.1, relheight=0.1)

    submit_btn = Button(question_canvas, text="Submit", font=card_btn_font, bg=btn_bg, command=submit)
    submit_btn.place(relx=0.72, rely=0.53, relwidth=0.1, relheight=0.1)

    back_btn = Button(quiz_canvas, text="Back", font=card_btn_font, bg=btn_bg, command=exit)
    back_btn.place(relx=0.9, rely=0.07, relwidth=0.07, relheight=0.05)

tnum = 0
def terms_tab():
    def previous():
        global tnum
        if tnum > 0:
            tnum -= 1
            update_display()

    def next():
        global tnum
        if tnum < len(data) - 1:
            tnum += 1
            update_display()

    def update_display():
        terms_count.config(text=f"{tnum + 1}/{len(data)}")
        term.config(text=data[tnum][0])
        term_info.config(text=str(data[tnum][2]))

    terms_canvas = Canvas(base, bg=base_bg)
    terms_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

    data = [('Liability :', 'Investment', "A liability is a debt or amount of money that an entity owes to another entity. \nExamples of liabilities include bank loans, accounts payable and credit card debts. \nCurrent liabilities are due within a year, while non-current liabilities are more\n long term, such as mortgages and leases. Much like assets, liabilities appear on\n businesses' balance sheets."), ('Loan :', 'Finance', 'A loan is a sum of money or an item that one entity lets another entity borrow.\n The borrower repays their debt to the lender within a specified period and may pay \ninterest on it. To take out a loan, an individual typically provides a lending organization with\n a reason for requesting the funds and includes some of their financial information, such as their \ncredit score and proof of employment.'), ('Interest :', 'Finance', "Interest is the additional money individuals must pay when borrowing money. \nInstitutions that loan money to an entity typically charge interest at a rate that\n is a percentage of the loan. For example, if an individual secures a $30,000 loan for\n a car, a lender may require them to pay an additional 5% of the loan back, or\n $1,500 in interest. Interest rates can also vary based on other factors, such as an\n individual's credit score and how long it takes them to repay the money."), ('Credit :', 'Finance', 'Credit is a contractual agreement in which a lender loans money to a\n borrower, understanding that the borrower intends to repay it later. A borrower can \ndemonstrate their trustworthiness in numerous ways, such as paying back their credit in full\n and on time consistently. Credit cards represent the most common example of buying on credit.'), ('Net worth :', 'Finance', "Net worth is the total value of what an individual or business owns minus the amount\n owed in debts. As a result, it represents the difference between an entity's assets and liabilities.\n Individuals can determine net worth by adding up the value\n of all their assets and subtracting their debt from that total.")]

    category_heading = Label(terms_canvas, text="Category : Finance", font=("Times New Roman", 50), bg=base_bg, fg=heading_fg)
    category_heading.place(relx=0.33, rely=0.06)

    term_mini_canvas = Canvas(base, bg=base_bg)
    term_mini_canvas.place(relx=0, rely=0.21, relheight=0.8, relwidth=1)

    terms_count = Label(term_mini_canvas, text="1/10", font=label_font, bg=base_bg, fg=label_fg)
    terms_count.place(relx=0.9, rely=0.06)

    term = Label(term_mini_canvas, text=data[tnum][0], font=term_font, bg=base_bg, fg=label_fg)
    term.place(relx=0.2, rely=0.1)

    term_info = Label(term_mini_canvas, text=str(data[tnum][2]), bg=base_bg, font=label_font, fg=label_fg)
    term_info.place(relx=0.2, rely=0.2)

    previous_btn = Button(term_mini_canvas, text="Previous", font=card_btn_font, bg=btn_bg, command=previous)
    previous_btn.place(relx=0.35, rely=0.53, relwidth=0.1, relheight=0.1)

    next_btn = Button(term_mini_canvas, text="Next", font=card_btn_font, bg=btn_bg, command=next)
    next_btn.place(relx=0.6, rely=0.53, relwidth=0.1, relheight=0.1)

    back_btn = Button(terms_canvas, text="Back", font=card_btn_font, bg=btn_bg, command=exit)
    back_btn.place(relx=0.9, rely=0.07, relwidth=0.07, relheight=0.05)

def goals_tab():
    def exit_add_goal():
        goals_tab()

    def add_goal_fun():
        amt = add_money.get()

        deposited = data[2]
        deposited = int(amt) + int(deposited)
        
        if int(deposited) <= int(data[1]):    
            query = "update goal set deposited=" + str(deposited) + " where status='yes'"
            con = sqlite3.connect("fls_db.db")
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
            con.close()
            remaining_amt.configure(text="Remaining Amount : " + str(int(data[1]) - (deposited)))

    goals_canvas = Canvas(base, bg=base_bg)
    goals_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

    def add_goal():
        def submit_goal_fun():
            title = goal_entry.get()
            amount = amt_entry.get()

            query = "update goal set status='no'"
            con = sqlite3.connect("fls_db.db")
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
            con.close()

            query = "insert into goal(title, total, deposited, status) values('" + title + "','" + amount + "', '0', 'yes')"
            con = sqlite3.connect("fls_db.db")
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
            con.close()
            goals_tab()

        add_goal_canvas = Canvas(goals_canvas, bg=base_bg)
        add_goal_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)  

        goal_title = Label(goals_canvas, text="Add Goal", font=term_font, bg=base_bg, fg=label_fg)
        goal_title.place(relx=0.45, rely=0.13)

        goal_lb = Label(add_goal_canvas, text="Enter Title : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        goal_lb.place(relx=0.3, rely=0.33)
        
        goal_entry = Entry(add_goal_canvas, font=entry_font, bg=entry_bg)
        goal_entry.place(relx=0.42, rely=0.332, relwidth=0.2, relheight=0.04)

        amt_lb = Label(add_goal_canvas, text="Enter Amount : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        amt_lb.place(relx=0.3, rely=0.43)
        
        amt_entry = Entry(add_goal_canvas, font=entry_font, bg=entry_bg)
        amt_entry.place(relx=0.42, rely=0.432, relwidth=0.2, relheight=0.04)

        submit_goal = Button(add_goal_canvas, text="Save", font=card_btn_font, bg=btn_bg, command=submit_goal_fun)
        submit_goal.place(relx=0.47, rely=0.53, relwidth=0.06, relheight=0.04)

        back_btn = Button(add_goal_canvas, text="Back", font=card_btn_font, bg=btn_bg, command=exit_add_goal)
        back_btn.place(relx=0.9, rely=0.07, relwidth=0.07, relheight=0.05)

    query = "select * from goal where status='yes'"
    con = sqlite3.connect("fls_db.db")
    cursor = con.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    con.commit()
    con.close()

    add_goal_btn = Button(goals_canvas, text="Add Goal", font=card_btn_font, bg=btn_bg, command=add_goal)
    add_goal_btn.place(relx=0.83, rely=0.1, relwidth=0.09, relheight=0.07)

    goal = Label(goals_canvas, text="Saving for : " + data[0], font=term_font, bg=base_bg, fg=label_fg)
    goal.place(relx=0.4, rely=0.13)

    add_money_lb = Label(goals_canvas, text="Add Money : ", font=small_lb_font, bg=base_bg, fg=label_fg)
    add_money_lb.place(relx=0.3, rely=0.33)
    
    add_money = Entry(goals_canvas, font=entry_font, bg=entry_bg)
    add_money.place(relx=0.4, rely=0.332, relwidth=0.2, relheight=0.04)

    add_money_btn = Button(goals_canvas, text="Save", font=card_btn_font, bg=btn_bg, command=add_goal_fun)
    add_money_btn.place(relx=0.63, rely=0.331, relwidth=0.06, relheight=0.04)

    total_amt = Label(goals_canvas, text="Total Amount : " + data[1], font=small_lb_font, bg=base_bg, fg=label_fg)
    total_amt.place(relx=0.3, rely=0.45)

    saved_amt = Label(goals_canvas, text="Amount Saved : "+ data[2], font=small_lb_font, bg=base_bg, fg=label_fg)
    saved_amt.place(relx=0.3, rely=0.52)

    remaining = int(data[1]) - int(data[2])

    remaining_amt = Label(goals_canvas, text="Remaining Amount : "+ str(remaining), font=small_lb_font, bg=base_bg, fg=label_fg)
    remaining_amt.place(relx=0.3, rely=0.59)

    ok_btn = Button(goals_canvas, text="Ok", font=card_btn_font, bg=btn_bg, command=exit)
    ok_btn.place(relx=0.47, rely=0.69, relwidth=0.09, relheight=0.07)

def calculators_tab():
    def emi_calci():
        def calculate_emi():
            principal_amount = float(loan_entry.get())
            interest_rate = float(interest_entry.get())
            tenure_m = float(tenure_entry.get())

            monthly_interest_rate = interest_rate / 12 / 100

            # Total number of monthly payments
            total_payments = tenure_m * 12

            # Calculate EMI using the formula: EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
            emi = principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments / \
                ((1 + monthly_interest_rate) ** total_payments - 1)

            # Calculate total amount paid and total interest paid
            total_amount_paid = emi * total_payments
            total_interest_paid = total_amount_paid - principal_amount

            monthly_emi.configure(text="Monthly EMI : " + str(int(emi)))
            principal_amt.configure(text="Principal Amount : " + str(int(principal_amount)))
            total_interest.configure(text="Total Interest : " + str(int(total_interest_paid)))
            total_amt.configure(text="Total Amount : " + str(int(total_amount_paid)))

        emi_canvas = Canvas(function_canvas, bg=base_bg)
        emi_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        emi_heading = Label(emi_canvas, text="EMI Calculator", font=term_font, bg=base_bg, fg=label_fg)
        emi_heading.place(relx=0.43, rely=0.03)

        loan_amt = Label(emi_canvas, text="Loan amount : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        loan_amt.place(relx=0.2, rely=0.15)
        
        loan_entry = Entry(emi_canvas, font=entry_font, bg=entry_bg)
        loan_entry.place(relx=0.42, rely=0.152, relwidth=0.2, relheight=0.04)

        interest_lb = Label(emi_canvas, text="Rate of Interest (p.a) : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        interest_lb.place(relx=0.2, rely=0.22)
        
        interest_entry = Entry(emi_canvas, font=entry_font, bg=entry_bg)
        interest_entry.place(relx=0.42, rely=0.222, relwidth=0.2, relheight=0.04)

        tenure_lb = Label(emi_canvas, text="Loan tenure (yrs) : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        tenure_lb.place(relx=0.2, rely=0.29)
        
        tenure_entry = Entry(emi_canvas, font=entry_font, bg=entry_bg)
        tenure_entry.place(relx=0.42, rely=0.292, relwidth=0.2, relheight=0.04)

        calculate_btn = Button(emi_canvas, text="Calculate", font=card_btn_font, bg=btn_bg, command=calculate_emi)
        calculate_btn.place(relx=0.47, rely=0.36, relwidth=0.09, relheight=0.07)

        monthly_emi = Label(emi_canvas, text="Monthly EMI :", font=label_font, bg=base_bg, fg=label_fg)
        monthly_emi.place(relx=0.23, rely=0.46)

        principal_amt = Label(emi_canvas, text="Principal Amount :", font=label_font, bg=base_bg, fg=label_fg)
        principal_amt.place(relx=0.23, rely=0.52)

        total_interest = Label(emi_canvas, text="Total Interest :", font=label_font, bg=base_bg, fg=label_fg)
        total_interest.place(relx=0.23, rely=0.59)

        total_amt = Label(emi_canvas, text="Total Amount :", font=label_font, bg=base_bg, fg=label_fg)
        total_amt.place(relx=0.23, rely=0.66)


    def sip_calci():
        def calculate_sip():
            investment_amount = float(investment_entry.get())
            annual_return_rate = float(return_entry.get())
            investment_period_years = float(period_entry.get())

            # Convert annual interest rate from percentage to decimal
            annual_interest_rate_decimal = annual_return_rate / 100

            # Monthly interest rate
            monthly_interest_rate = annual_interest_rate_decimal / 12

            # Calculate total number of monthly investments
            total_investments = investment_amount * investment_period_years * 12

            # Calculate estimated returns using the formula: A = P * [(1 + r)^nt - 1] / r
            returns = investment_amount * (((1 + monthly_interest_rate) ** (investment_period_years * 12)) - 1) / monthly_interest_rate

            # Calculate total value (total invested amount + total returns)
            total_value = total_investments + returns

            investment_amt.configure(text="Investment Amount: " + str(int(total_investments)))
            return_amt.configure(text="Returns: " + str(int(returns)))
            total_value_label.configure(text="Total Value: " + str(int(total_value)))

        sip_canvas = Canvas(function_canvas, bg=base_bg)
        sip_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        emi_heading = Label(sip_canvas, text="SIP Calculator", font=term_font, bg=base_bg, fg=label_fg)
        emi_heading.place(relx=0.43, rely=0.03)

        monthly_investment = Label(sip_canvas, text="Monthly Investment : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        monthly_investment.place(relx=0.2, rely=0.15)
        
        investment_entry = Entry(sip_canvas, font=entry_font, bg=entry_bg)
        investment_entry.place(relx=0.42, rely=0.152, relwidth=0.2, relheight=0.04)

        return_rate = Label(sip_canvas, text="Exp. return rate (p.a) : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        return_rate.place(relx=0.2, rely=0.22)
        
        return_entry = Entry(sip_canvas, font=entry_font, bg=entry_bg)
        return_entry.place(relx=0.42, rely=0.222, relwidth=0.2, relheight=0.04)

        period_lb = Label(sip_canvas, text="Time period (yrs) : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        period_lb.place(relx=0.2, rely=0.29)
        
        period_entry = Entry(sip_canvas, font=entry_font, bg=entry_bg)
        period_entry.place(relx=0.42, rely=0.292, relwidth=0.2, relheight=0.04)

        calculate_btn = Button(sip_canvas, text="Calculate", font=card_btn_font, bg=btn_bg, command=calculate_sip)
        calculate_btn.place(relx=0.47, rely=0.36, relwidth=0.09, relheight=0.07)

        investment_amt = Label(sip_canvas, text="Investment Amount : ", font=label_font, bg=base_bg, fg=label_fg)
        investment_amt.place(relx=0.23, rely=0.46)

        return_amt = Label(sip_canvas, text="Est. returns : ", font=label_font, bg=base_bg, fg=label_fg)
        return_amt.place(relx=0.23, rely=0.52)

        total_value_label = Label(sip_canvas, text="Total Value :", font=label_font, bg=base_bg, fg=label_fg)
        total_value_label.place(relx=0.23, rely=0.58)

    def fd_calci():
        def calculate_fd():
            # Get inputs from the user
            investment_amount = float(investment_entry.get())
            annual_interest_rate = float(return_entry.get())
            investment_period_years = float(period_entry.get())

            # Calculate FD details
            total_invested_amount = investment_amount * investment_period_years
            returns = (investment_amount * annual_interest_rate * investment_period_years) / 100
            total_amt = total_invested_amount + returns

            # Update labels with the calculated values
            investment_amt.configure("Investment Amount : " + str(total_invested_amount))
            return_amt.configure("Est. Returns : " + str(returns))
            total_value.configure("Total Value : " + str(total_amt))

        fd_canvas = Canvas(function_canvas, bg=base_bg)
        fd_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        emi_heading = Label(fd_canvas, text="FD Calculator", font=term_font, bg=base_bg, fg=label_fg)
        emi_heading.place(relx=0.39, rely=0.03)

        monthly_investment = Label(fd_canvas, text="Monthly Investment : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        monthly_investment.place(relx=0.2, rely=0.15)
        
        investment_entry = Entry(fd_canvas, font=entry_font, bg=entry_bg)
        investment_entry.place(relx=0.42, rely=0.152, relwidth=0.2, relheight=0.04)

        interest_rate = Label(fd_canvas, text="Rate of Interest (p.a) : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        interest_rate.place(relx=0.2, rely=0.22)
        
        return_entry = Entry(fd_canvas, font=entry_font, bg=entry_bg)
        return_entry.place(relx=0.42, rely=0.222, relwidth=0.2, relheight=0.04)

        period_lb = Label(fd_canvas, text="Time period (yrs) : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        period_lb.place(relx=0.2, rely=0.29)
        
        period_entry = Entry(fd_canvas, font=entry_font, bg=entry_bg)
        period_entry.place(relx=0.42, rely=0.292, relwidth=0.2, relheight=0.04)

        calculate_btn = Button(fd_canvas, text="Calculate", font=card_btn_font, bg=btn_bg, command=calculate_fd)
        calculate_btn.place(relx=0.47, rely=0.36, relwidth=0.09, relheight=0.07)

        investment_amt = Label(fd_canvas, text="Investment Amount : ", font=label_font, bg=base_bg, fg=label_fg)
        investment_amt.place(relx=0.23, rely=0.46)

        return_amt = Label(fd_canvas, text="Est. returns : ", font=label_font, bg=base_bg, fg=label_fg)
        return_amt.place(relx=0.23, rely=0.52)

        total_value = Label(fd_canvas, text="Total Value :", font=label_font, bg=base_bg, fg=label_fg)
        total_value.place(relx=0.23, rely=0.58)

    calci_canvas = Canvas(base, bg=base_bg)
    calci_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

    heading = Label(calci_canvas, text="Financial Calculators", font=("Times New Roman", 50), bg=base_bg, fg=heading_fg)
    heading.place(relx=0.32, rely=0.05)

    back_btn = Button(calci_canvas, text="Back", font=card_btn_font, bg=btn_bg, command=exit)
    back_btn.place(relx=0.9, rely=0.07, relwidth=0.07, relheight=0.05)

    function_canvas = Canvas(base, bg=base_bg)
    function_canvas.place(relx=0.199, rely=0.198, relwidth=0.8, relheight=1)

    btn_canvas = Canvas(base, bg=btn_canvas_bg)
    btn_canvas.place(relx=0, rely=0.198, relwidth=0.2, relheight=1)

    emi_calci()

    btn1 = Button(btn_canvas, text="EMI", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=emi_calci)
    btn1.place(relx=0, rely=0, relwidth=1, relheight=0.05)

    btn2 = Button(btn_canvas, text="SIP", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=sip_calci)
    btn2.place(relx=0, rely=0.05, relwidth=1, relheight=0.05)

    btn3 = Button(btn_canvas, text="Fixed Deposit", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=fd_calci)
    btn3.place(relx=0, rely=0.10, relwidth=1, relheight=0.05)

    btn4 = Button(btn_canvas, text="Recurring Deposit", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt)
    btn4.place(relx=0, rely=0.15, relwidth=1, relheight=0.05)


def banking_tab():
    def deposit():
        def deposit_fun():
            con = sqlite3.connect("fls_db.db")
            q = "select * from transactions"
            cursor = con.cursor()
            cursor.execute(q)
            data = cursor.fetchone()
            con.commit()

            amount = amount_entry.get()
            pin_inp = pin_entry.get()
            balance = data[3]
            balance = int(balance) + int(amount)

            con = sqlite3.connect("fls_db.db")
            q = "select * from account"
            cursor = con.cursor()
            cursor.execute(q)
            pin_tuple = cursor.fetchone()
            con.commit()
            pin = pin_tuple[7]

            if pin_inp == pin:
                q = "update transactions set balance =" + str(balance)
                cursor = con.cursor()
                cursor.execute(q)
                data = cursor.fetchone()
                con.commit()
                remaining_bal.configure(text="Remaining Balance : " + str(balance))

            else:
                messagebox.showerror("PIN", "Please Enter Correct PIN")

        def withdraw_fun():
            con = sqlite3.connect("fls_db.db")
            q = "select * from transactions"
            cursor = con.cursor()
            cursor.execute(q)
            data = cursor.fetchone()
            con.commit()

            amount = amount_entry.get()
            pin_inp = pin_entry.get()
            balance = data[3]
            balance = int(balance) - int(amount)

            con = sqlite3.connect("fls_db.db")
            q = "select * from account"
            cursor = con.cursor()
            cursor.execute(q)
            pin_tuple = cursor.fetchone()
            con.commit()
            pin = pin_tuple[7]

            if pin_inp == pin:
                q = "update transactions set balance =" + str(balance)
                cursor = con.cursor()
                cursor.execute(q)
                data = cursor.fetchone()
                con.commit()
                remaining_bal.configure(text="Remaining Balance : " + str(balance))
            
            else:
                messagebox.showerror("PIN", "Please Enter Correct PIN")


        deposit_canvas = Canvas(function_canvas, bg=base_bg)
        deposit_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        deposit_heading = Label(deposit_canvas, text="Deposit / Withdraw", font=term_font, bg=base_bg, fg=label_fg)
        deposit_heading.place(relx=0.39, rely=0.03)

        amount = Label(deposit_canvas, text="Enter amount : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        amount.place(relx=0.2, rely=0.15)
        
        amount_entry = Entry(deposit_canvas, font=entry_font, bg=entry_bg)
        amount_entry.place(relx=0.42, rely=0.152, relwidth=0.2, relheight=0.04)

        pin = Label(deposit_canvas, text="Enter PIN : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        pin.place(relx=0.2, rely=0.22)
        
        pin_entry = Entry(deposit_canvas, font=entry_font, bg=entry_bg)
        pin_entry.place(relx=0.42, rely=0.222, relwidth=0.2, relheight=0.04)

        deposit_btn = Button(deposit_canvas, text="Deposit", font=card_btn_font, bg=btn_bg, command=deposit_fun)
        deposit_btn.place(relx=0.35, rely=0.36, relwidth=0.09, relheight=0.07)

        withdraw_btn = Button(deposit_canvas, text="Withdraw", font=card_btn_font, bg=btn_bg, command=withdraw_fun)
        withdraw_btn.place(relx=0.55, rely=0.36, relwidth=0.09, relheight=0.07)

        remaining_bal = Label(deposit_canvas, text="Remaining Balance : ", font=label_font, bg=base_bg, fg=label_fg)
        remaining_bal.place(relx=0.23, rely=0.5)

    def balance():
        def check_balance():
            con = sqlite3.connect("fls_db.db")
            q = "select * from account"
            cursor = con.cursor()
            cursor.execute(q)
            pin_tuple = cursor.fetchone()
            con.commit()
            pin = pin_tuple[7]

            con = sqlite3.connect("fls_db.db")
            q = "select * from transactions"
            cursor = con.cursor()
            cursor.execute(q)
            data = cursor.fetchone()
            con.commit()
            con.close()

            pin_inp = pin_entry.get()    
            balance = data[3]

            if pin_inp == pin:
                remaining_bal.configure(text="Remaining Balance : " + str(balance))
            else:
                messagebox.showerror("PIN", "Please Enter Correct PIN")

        balance_canvas = Canvas(function_canvas, bg=base_bg)
        balance_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        deposit_heading = Label(balance_canvas, text="Balance Inquiry", font=term_font, bg=base_bg, fg=label_fg)
        deposit_heading.place(relx=0.39, rely=0.03)

        pin = Label(balance_canvas, text="Enter PIN : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        pin.place(relx=0.2, rely=0.22)
        
        pin_entry = Entry(balance_canvas, font=entry_font, bg=entry_bg)
        pin_entry.place(relx=0.42, rely=0.222, relwidth=0.2, relheight=0.04)

        check_btn = Button(balance_canvas, text="Check Balance", font=card_btn_font, bg=btn_bg, command=check_balance)
        check_btn.place(relx=0.42, rely=0.33, relwidth=0.18, relheight=0.07)

        remaining_bal = Label(balance_canvas, text="Remaining Balance : ", font=label_font, bg=base_bg, fg=label_fg)
        remaining_bal.place(relx=0.23, rely=0.5)
    
    def pin_change():
        def change_pin():
            current_pin = cur_pin_entry.get()
            new_pin = new_pin_entry.get()
            confirm_pin = confirm_pin_entry.get()
            
            con = sqlite3.connect("fls_db.db")
            q = "select * from account"
            cursor = con.cursor()
            cursor.execute(q)
            pin_tuple = cursor.fetchone()
            con.commit()
            pin = pin_tuple[7]

            if current_pin == pin and new_pin == confirm_pin:
                con = sqlite3.connect("fls_db.db")
                q = "update account set pin =" + str(new_pin)
                cursor = con.cursor()
                cursor.execute(q)
                pin_tuple = cursor.fetchone()
                con.commit()
                con.close()
                messagebox.showinfo("PIN", "PIN changed successfully")

            else:
                messagebox.showerror("PIN", "Please Enter Correct PIN")
            

        pin_canvas = Canvas(function_canvas, bg=base_bg)
        pin_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        deposit_heading = Label(pin_canvas, text="PIN Change", font=term_font, bg=base_bg, fg=label_fg)
        deposit_heading.place(relx=0.39, rely=0.03)

        cur_pin = Label(pin_canvas, text="Enter Current PIN : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        cur_pin.place(relx=0.2, rely=0.15)
        
        cur_pin_entry = Entry(pin_canvas, font=entry_font, bg=entry_bg)
        cur_pin_entry.place(relx=0.42, rely=0.152, relwidth=0.2, relheight=0.04)

        new_pin = Label(pin_canvas, text="Enter New PIN : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        new_pin.place(relx=0.2, rely=0.22)
        
        new_pin_entry = Entry(pin_canvas, font=entry_font, bg=entry_bg)
        new_pin_entry.place(relx=0.42, rely=0.222, relwidth=0.2, relheight=0.04)

        confirm_pin = Label(pin_canvas, text="Confirm PIN : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        confirm_pin.place(relx=0.2, rely=0.29)
        
        confirm_pin_entry = Entry(pin_canvas, font=entry_font, bg=entry_bg)
        confirm_pin_entry.place(relx=0.42, rely=0.292, relwidth=0.2, relheight=0.04)

        change_btn = Button(pin_canvas, text="Change PIN", font=card_btn_font, bg=btn_bg, command=change_pin)
        change_btn.place(relx=0.37, rely=0.4, relwidth=0.18, relheight=0.07)

    def fd():

        def current_fd():
            current_fd_canvas = Canvas(fd_canvas, bg=base_bg)
            current_fd_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
            
            deposit_heading = Label(fd_canvas, text="Current FD", font=term_font, bg=base_bg, fg=label_fg)
            deposit_heading.place(relx=0.39, rely=0.03)

            back_btn = Button(current_fd_canvas, text="Back", font=card_btn_font, bg=btn_bg, command=fd)
            back_btn.place(relx=0.9, rely=0.07, relwidth=0.07, relheight=0.05)

            date = Label(fd_canvas, text="Date : ", font=small_lb_font, bg=base_bg, fg=label_fg)
            date.place(relx=0.2, rely=0.15)

            percentage = Label(fd_canvas, text="Interest Rate : 6.5%", font=small_lb_font, bg=base_bg, fg=label_fg)
            percentage.place(relx=0.2, rely=0.22)

            interest_eared = Label(fd_canvas, text="Interest Earned : ", font=small_lb_font, bg=base_bg, fg=label_fg)
            interest_eared.place(relx=0.2, rely=0.29)

            total_amount = Label(fd_canvas, text="Total Amount : ", font=small_lb_font, bg=base_bg, fg=label_fg)
            total_amount.place(relx=0.2, rely=0.36)

        fd_canvas = Canvas(function_canvas, bg=base_bg)
        fd_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        deposit_heading = Label(fd_canvas, text="Fixed Deposit", font=term_font, bg=base_bg, fg=label_fg)
        deposit_heading.place(relx=0.39, rely=0.03)

        current_fd_btn = Button(fd_canvas, text="Current FD", font=card_btn_font, bg=btn_bg, command=current_fd)
        current_fd_btn.place(relx=0.8, rely=0.05, relwidth=0.13, relheight=0.07)

        amount = Label(fd_canvas, text="Enter amount : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        amount.place(relx=0.2, rely=0.15)
        
        amount_entry = Entry(fd_canvas, font=entry_font, bg=entry_bg)
        amount_entry.place(relx=0.42, rely=0.152, relwidth=0.2, relheight=0.04)

        period = Label(fd_canvas, text="Time Period (yrs) : ", font=small_lb_font, bg=base_bg, fg=label_fg)
        period.place(relx=0.2, rely=0.22)
        
        period_entry = Entry(fd_canvas, font=entry_font, bg=entry_bg)
        period_entry.place(relx=0.42, rely=0.222, relwidth=0.2, relheight=0.04)

        confirm_btn = Button(fd_canvas, text="Confirm", font=card_btn_font, bg=btn_bg)
        confirm_btn.place(relx=0.35, rely=0.36, relwidth=0.09, relheight=0.07)

        calculate_btn = Button(fd_canvas, text="Calculate", font=card_btn_font, bg=btn_bg)
        calculate_btn.place(relx=0.55, rely=0.36, relwidth=0.09, relheight=0.07)

        interest_earned = Label(fd_canvas, text="Est. Interest Earned : ", font=label_font, bg=base_bg, fg=label_fg)
        interest_earned.place(relx=0.23, rely=0.5)

        total_amount = Label(fd_canvas, text="Total Amount : ", font=label_font, bg=base_bg, fg=label_fg)
        total_amount.place(relx=0.23, rely=0.58)
    
    def transaction():
        transaction_canvas = Canvas(function_canvas, bg=base_bg)
        transaction_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        transaction_heading = Label(transaction_canvas, text="Transaction History", font=term_font, bg=base_bg, fg=label_fg)
        transaction_heading.place(relx=0.39, rely=0.03)

        table_canvas = Canvas(transaction_canvas, bg=entry_bg)
        table_canvas.place(relx=0.13, rely=0.14, relwidth=0.8, relheight=0.55)

        scroll = Scrollbar(transaction_canvas, orient='vertical')

        # Creating Table
        table = ttk.Treeview(table_canvas, columns=("Date", "Credit", "Debit"), show="headings", yscrollcommand=scroll.set)
        table.place(relheight=1, relwidth=1)

        table.column(0, anchor=CENTER)
        table.column(1, anchor=CENTER)
        table.column(2, anchor=CENTER)

        table.heading(0, text="Date")
        table.heading(1, text="Credit")
        table.heading(2, text="Debit")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Helvetica", 15))
        style.configure(".", font=("Helvetica", 13), rowheight=35)
        '''
        for item in table.get_children():
            table.delete(item)
                                                    
        for eachline in sub_data:
            table.insert("", END, values=(eachline[0], eachline[1]))
        '''


    def details():
        con = sqlite3.connect("fls_db.db")
        q = "select * from account"
        cursor = con.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        con.commit()
        con.close()

        details_canvas = Canvas(function_canvas, bg=base_bg)
        details_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        details_heading = Label(details_canvas, text="Account Details", font=term_font, bg=base_bg, fg=label_fg)
        details_heading.place(relx=0.39, rely=0.03)

        name = Label(details_canvas, text="Account Holder : " + data[0], font=small_lb_font, bg=base_bg, fg=label_fg)
        name.place(relx=0.2, rely=0.15)

        acn_number = Label(details_canvas, text="Account Number : " + data[1], font=small_lb_font, bg=base_bg, fg=label_fg)
        acn_number.place(relx=0.2, rely=0.22)

        dob = Label(details_canvas, text="DOB : " + data[2], font=small_lb_font, bg=base_bg, fg=label_fg)
        dob.place(relx=0.2, rely=0.29)

        acn_type = Label(details_canvas, text="Account Type : " + data[3], font=small_lb_font, bg=base_bg, fg=label_fg)
        acn_type.place(relx=0.2, rely=0.36)

        email = Label(details_canvas, text="Email : " + data[4], font=small_lb_font, bg=base_bg, fg=label_fg)
        email.place(relx=0.2, rely=0.43)

        mob_num = Label(details_canvas, text="Mobile number : " + data[5], font=small_lb_font, bg=base_bg, fg=label_fg)
        mob_num.place(relx=0.2, rely=0.5)

        address = Label(details_canvas, text="Address : " + data[6], font=small_lb_font, bg=base_bg, fg=label_fg)
        address.place(relx=0.2, rely=0.57)

    con = sqlite3.connect("fls_db.db")
    q = "select * from account"
    cursor = con.cursor()
    cursor.execute(q)
    data = cursor.fetchone()
    con.commit()
    con.close()

    banking_canvas = Canvas(base, bg=base_bg)
    banking_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

    heading = Label(banking_canvas, text="Banking Simulation", font=("Times New Roman", 50), bg=base_bg, fg=heading_fg)
    heading.place(relx=0.32, rely=0.05)

    name = Label(banking_canvas, text="Acn. Holder : " + data[0], font=small_lb_font, bg=base_bg, fg=label_fg)
    name.place(relx=0.01, rely=0.05)
    
    account_num = Label(banking_canvas, text="Acn. Number : " + data[1], font=small_lb_font, bg=base_bg, fg=label_fg)
    account_num.place(relx=0.01, rely=0.1)

    back_btn = Button(banking_canvas, text="Back", font=card_btn_font, bg=btn_bg, command=exit)
    back_btn.place(relx=0.9, rely=0.07, relwidth=0.07, relheight=0.05)

    function_canvas = Canvas(base, bg=base_bg)
    function_canvas.place(relx=0.199, rely=0.198, relwidth=0.8, relheight=1)

    btn_canvas = Canvas(base, bg=btn_canvas_bg)
    btn_canvas.place(relx=0, rely=0.198, relwidth=0.2, relheight=1)

    btn1 = Button(btn_canvas, text="Account Details", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=details)
    btn1.place(relx=0, rely=0, relwidth=1, relheight=0.05)

    btn2 = Button(btn_canvas, text="Deposit / Withdraw", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=deposit)
    btn2.place(relx=0, rely=0.05, relwidth=1, relheight=0.05)

    btn3 = Button(btn_canvas, text="Check Balance", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=balance)
    btn3.place(relx=0, rely=0.1, relwidth=1, relheight=0.05)

    btn4 = Button(btn_canvas, text="PIN change", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=pin_change)
    btn4.place(relx=0, rely=0.15, relwidth=1, relheight=0.05)

    # btn5 = Button(btn_canvas, text="Fixed Deposit", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=fd)
    # btn5.place(relx=0, rely=0.2, relwidth=1, relheight=0.05)

    # btn6 = Button(btn_canvas, text="Transaction History", bg=fun_btn_bg, fg=fun_btn_fg, font=fun_btn_fnt, command=transaction)
    # btn6.place(relx=0, rely=0.25, relwidth=1, relheight=0.05)

    details()



base = Tk()
base.title("Financial Literacy Simulator")
base.minsize(width=1000, height=700)
base.geometry("1920x1080")
base.configure(background="#FEFAE0")
base.wm_state('zoomed')

def main_window():
    heading_canvas = Canvas(base, bg=base_bg)
    heading_canvas.place(relx=0, rely=0, relwidth=1,relheight=0.15)

    heading = Label(heading_canvas, text="Financial Literacy Simulator", font=("Times New Roman", 50), bg=base_bg, fg=heading_fg)
    heading.place(relx=0.24, rely=0.17)

    card_canvas = Canvas(base, bg=base_bg)
    card_canvas.place(relx=0, rely=0.15, relwidth=1,relheight=1)

    # First Card
    quiz_card = Canvas(base, bg=base_bg)
    quiz_card.place(relx=0.15, rely=0.22, relwidth=0.18,relheight=0.3)

    quiz_lb = Label(quiz_card, text="Financial Quiz", bg=base_bg, font=label_font, fg=label_fg)
    quiz_lb.place(relx=0.18, rely=0.3)

    quiz_card_btn = Button(quiz_card, text="Play", font=card_btn_font, bg=btn_bg, command=quiz_tab)
    quiz_card_btn.place(relx=0.24, rely=0.53, relwidth=0.5, relheight=0.15)
    # END First Card

    # Second Card
    banking_card = Canvas(base, bg=base_bg)
    banking_card.place(relx=0.4, rely=0.22, relwidth=0.18,relheight=0.3)

    banking_lb = Label(banking_card, text="Banking", bg=base_bg, font=label_font, fg=label_fg)
    banking_lb.place(relx=0.3, rely=0.3)

    banking_card_btn = Button(banking_card, text="Play", font=card_btn_font, bg=btn_bg, command=banking_tab)
    banking_card_btn.place(relx=0.24, rely=0.53, relwidth=0.5, relheight=0.15)
    # END Second Card

    # Third Card
    calci_card = Canvas(base, bg=base_bg)
    calci_card.place(relx=0.65, rely=0.22, relwidth=0.18,relheight=0.3)

    calci_lb = Label(calci_card, text="Calculators", bg=base_bg, font=label_font, fg=label_fg)
    calci_lb.place(relx=0.22, rely=0.3)

    calci_card_btn = Button(calci_card, text="Play", font=card_btn_font, bg=btn_bg, command=calculators_tab)
    calci_card_btn.place(relx=0.24, rely=0.53, relwidth=0.5, relheight=0.15)
    # END Third Card

    # Fourth Card
    terms_card = Canvas(base, bg=base_bg)
    terms_card.place(relx=0.27, rely=0.585, relwidth=0.18,relheight=0.3)

    terms_lb = Label(terms_card, text="Fin. Terminologies", bg=base_bg, font=label_font, fg=label_fg)
    terms_lb.place(relx=0.11, rely=0.3)

    terms_card_btn = Button(terms_card, text="Play", font=card_btn_font, bg=btn_bg, command=terms_tab)
    terms_card_btn.place(relx=0.24, rely=0.53, relwidth=0.5, relheight=0.15)
    # END Fourth Card

    # Fifth Card
    goals_card = Canvas(base, bg=base_bg)
    goals_card.place(relx=0.5, rely=0.585, relwidth=0.18,relheight=0.3)

    goals_lb = Label(goals_card, text="Your Goals", bg=base_bg, font=label_font, fg=label_fg)
    goals_lb.place(relx=0.22, rely=0.3)

    goals_card_btn = Button(goals_card, text="Play", font=card_btn_font, bg=btn_bg, command=goals_tab)
    goals_card_btn.place(relx=0.24, rely=0.53, relwidth=0.5, relheight=0.15)
    # END Fifth Card

    base.mainloop()

# Calling Main Window
main_window()