from flask import Flask, request, render_template, url_for, make_response
import inov

app = Flask(__name__, template_folder="templates")


# welcome page
@app.route('/')
def welcome():
    if request.args.values() == 'Create Account':
        return make_response(url_for('create_acc_choice'))
    if request.args.values() == 'Send Money':
        return make_response(url_for('send_money'))
    if request.args.values() == 'Deposit':
        return make_response(url_for('deposit'))
    return render_template('intro.html')


# Choose account you want to create
@app.route('/create_accounts_choice', methods={'POST', 'GET'})
def create_acc_choice():
    if request.method == 'POST':
        if request.args.values() == 'Debit':
            return make_response(url_for('debit_accnt_created'))
        if request.args.values() == 'Credit':
            return make_response(url_for('credit_accnt_created'))
        if request.args.values() == 'International Debit':
            return make_response(url_for('inter_debit_accnt_created'))
    return render_template('createaccnt.html')


# create credit account
@app.route('/credit_user_created', methods={'POST', 'GET'})
def credit_accnt_created():
    if request.method == 'POST' and request.args.values() == 'create credit account':
        name = request.form.get("credit_nm")
        email = request.form.get("credit_email")
        address = request.form.get("credit_address")
        checking = request.form.get("credit_checkings")
        saving = request.form.get("credit_savings")
        return inov.create_Credit_account(name, email, address, checking, saving)
    return render_template("CreditAccount.html")


# create debit account
@app.route('/debit_user_created', methods={'POST', 'GET'})
def debit_accnt_created():
    if request.method == 'POST':
        name = request.form.get("debit_nm")
        email = request.form.get("debit_email")
        address = request.form.get("debit_address")
        checking = request.form.get("debit_checkings")
        saving = request.form.get("debit_savings")
        return inov.create_Debit_account(name, email, address, checking, saving)
    return render_template("DebitAccount.html")


# create international debit (outside US) account
@app.route('/International_debit_user_created', methods={'POST', 'GET'})
def inter_debit_accnt_created():
    if request.method == 'POST':
        name = request.form.get("debit_nm")
        email = request.form.get("debit_email")
        address = request.form.get("debit_address")
        checking = request.form.get("debit_checkings")
        saving = request.form.get("debit_savings")
        return inov.create_Debit_account(name, email, address, checking, saving)
    return render_template("InternationalDebitAccount.html")


# deposit money into account
@app.route('/deposit_option', methods={'POST', 'GET'})
def deposit_option():
    if request.args.values() == 'Yes':
        return make_response(url_for('deposit_International'))
    if request.args.values() == 'No':
        return make_response(url_for('deposit'))
    return render_template('depositOption.html')


@app.route('/deposit', methods={'POST', 'GET'})
def deposit():
    if request.method == 'POST':
        card_num = request.form['Virtual card number']
        amount = request.form['amount']
        if request.args.values() == 'deposit':
            return inov.deposit_Checking(amount, card_num)
    return render_template('deposit.html')


@app.route('/deposit_International', methods={'POST', 'GET'})
def deposit_International():
    if request.args.values() == 'Yes':
        return
    return render_template('depositOption.html')


# send money
@app.route('/send_money_option', methods={'POST', 'GET'})
def send_option():
    if request.args.values() == 'Yes':
        return make_response(url_for('send_money_InternationalDebit'))
    if request.args.values() == 'No':
        return make_response(url_for('send_money_credit'))
    if request.args.values() == 'International Debit account':
        return make_response(url_for('send_money_InternationalDebit'))
    return render_template('sendOption.html')


@app.route('/send_money_option2', methods={'POST', 'GET'})
def send_option2():
    if request.args.values() == 'Yes':
        return make_response(url_for('send_option3'))
    if request.args.values() == 'No':
        return make_response(url_for('send_money_credit'))
    if request.args.values() == 'International Debit account':
        return make_response(url_for('send_money_InternationalDebit'))
    return render_template('sendOption2.html')


@app.route('/send_money_option3', methods={'POST', 'GET'})
def send_option3():
    if request.args.values() == 'Debit account':
        return make_response(url_for('send_money_debit_International'))
    if request.args.values() == 'Credit account':
        return make_response(url_for('send_money_credit'))
    if request.args.values() == 'International Debit account':
        return make_response(url_for('send_money_credit_International'))
    return render_template('sendOption3.html')


@app.route('/send money', methods={'POST', 'GET'})
def send_money():
    if request.args.values() == 'Debit account':
        return make_response(url_for('send_money_debit'))
    if request.args.values() == 'Credit account':
        return make_response(url_for('send_money_credit'))
    return render_template('send.html')


@app.route('/send_money_debit', methods={'POST', 'GET'})
def send_money_debit():
    if request.method == 'POST':
        debit_card_num = request.form['virtual_debit_card_num']
        debit_receiver_name = request.form['debit_rec_name']
        debit_amount = request.form['debit_amount']
        return inov.send_money_Debit(debit_amount, debit_card_num, debit_receiver_name)
    return render_template('debit_send.html')


@app.route('/send_money_debit_International', methods={'POST', 'GET'})
def send_money_debit_International():
    if request.method == 'POST':
        debit_card_num = request.form['virtual_debit_card_num']
        debit_receiver_name = request.form['debit_rec_name']
        debit_amount = request.form['debit_amount']
        debit_country = request.form['Inter_debit_Country']
        return inov.international_send_debit(debit_amount, debit_card_num, debit_receiver_name, debit_country)
    return render_template('sendDebitInter.html')


@app.route('/send_money_credit', methods={'POST', 'GET'})
def send_money_credit():
    if request.method == 'POST':
        credit_card_num = request.form['virtual_credit_name']
        credit_receiver_name = request.form['credit_rec_name']
        credit_amount = request.form['credit_amount']
        return inov.send_money_Credit(credit_amount, credit_card_num, credit_receiver_name)
    return render_template('credit_send.html')


@app.route('/send_money_credit_International', methods={'POST', 'GET'})
def send_money_credit_International():
    if request.method == 'POST':
        credit_card_num = request.form['virtual_credit_name']
        credit_receiver_name = request.form['credit_rec_name']
        credit_amount = request.form['credit_amount']
        credit_country = request.form['Inter_debit_Country']
        return inov.international_send_credit(credit_amount, credit_card_num, credit_receiver_name, credit_country)
    return render_template('sendCreditInter.html')


@app.route('/send money', methods={'POST', 'GET'})
def send_money_InternationalDebit():
    if request.method == 'POST':
        inter_debit_card_num = request.form['Inter_virtual_debit_card_num']
        inter_debit_receiver_name = request.form['Inter_debit_rec_name']
        inter_debit_amount = request.form['Inter_debit_amount']
        inter_debit_country = request.form['Inter_debit_Country']
        inter_debit_code = request.form['Inter_debit_Country_code']
        return inov.international_debit_send(inter_debit_amount, inter_debit_receiver_name, inter_debit_card_num,
                                             inter_debit_code, inter_debit_country)
    return render_template('inter_send.html')


if __name__ == '__main__':
    app.run(debug=True)

