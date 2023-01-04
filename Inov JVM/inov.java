import javax.crypto.KeyGenerator;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import java.io.IOException;
import javax.mail.internet.AddressException;
//import java.math.BigDecimal;
import java.io.UnsupportedEncodingException;
import java.security.Key;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.sql.*;
import java.util.Currency;
import java.util.Properties;
import java.util.Scanner;
import java.math.*;
import java.time.LocalDate;



public class inov {
    invp pay = new invp();
    CurrenciesCurrencyExchange chan = new CurrenciesCurrencyExchange();
    Currencies current = new Currencies();
    BDMS bdms = new BDMS();
    InterCreditDebit tran = new InterCreditDebit();
    public Connection connect() throws SQLException {
        try {
            Class.forName("org.postgresql.Driver");
            Connection connection = DriverManager.getConnection("jdbc:postgresql://localhost/inovjava", "postgres", "");
            System.out.println("Connecting to network.");
            return connection;
        } catch (SQLException e) {
            throw new RuntimeException("Cannot connect to network", e);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }


    public static void intro() {
        System.out.println("WELCOME TO INOV!!!!!! We are a SaaS startup that build creative, innovative and simpler apis for more transparent financial services. " +
                "We only operate in the US as of right now but we look to expand.");
    }

    public void create_debit_account(String name, String email, String address, double checking, double saving) throws NoSuchAlgorithmException {
        //Country
        Currency usa = Currency.getInstance("USD");
        String curr_code = usa.getCurrencyCode();
        // Read input scan
        Scanner scan = new Scanner(System.in);
        //Creating a KeyGenerator object Cryptography key
        KeyGenerator keyGen = KeyGenerator.getInstance("DES");

        //Creating a SecureRandom object
        SecureRandom secRandom = new SecureRandom();

        //Initializing the KeyGenerator
        keyGen.init(secRandom);

        //Creating/Generating a key
        Key key = keyGen.generateKey();
        String secure_code = key.toString();
        String get_code = secure_code.substring(28);
        // System.out.println(get_code);
        //create account details
        int card_num = secRandom.nextInt(11111);
        //Insert inputs into database Table (creating account)
        String read_data = "INSERT INTO InovDEBIT(NAME, EMAIL, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY) VALUES (?, ?, ?, ?, ?, ?, ?, ?);";
        try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(read_data)) {
            pstmt.setString(1, name);
            pstmt.setString(2, email);
            pstmt.setInt(3, card_num);
            pstmt.setString(4, get_code);
            pstmt.setDouble(5, checking);
            pstmt.setDouble(6, saving);
            pstmt.setString(7, address);
            pstmt.setString(8, curr_code);
            pstmt.executeUpdate();
            System.out.println("Debit Account created");
            //send_mail_new_Account_Debit(email, card_num, get_code);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
        // mail notification



    public void create_International_debit_account(String name, String email, String address, String Country, double checking, double saving) throws NoSuchAlgorithmException {
        // Read input scan
        Scanner scan = new Scanner(System.in);
        //Creating a KeyGenerator object Cryptography key
        KeyGenerator keyGen = KeyGenerator.getInstance("DES");

        //Creating a SecureRandom object
        SecureRandom secRandom = new SecureRandom();

        //Initializing the KeyGenerator
        keyGen.init(secRandom);

        //Creating/Generating a key
        Key key = keyGen.generateKey();
        String secure_code = key.toString();
        String get_code = secure_code.substring(28);
        // System.out.println(get_code);
        //create account details
        int card_num = secRandom.nextInt(11111);
        String read_data = "INSERT INTO InovInterDEBIT(NAME, EMAIL, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY) VALUES " +
                    "(?, ?, ?, ?, ?, ?, ?, ?)";
        try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(read_data)) {
            pstmt.setString(1, name);
            pstmt.setString(2, email);
            pstmt.setInt(3, card_num);
            pstmt.setString(4, get_code);
            pstmt.setDouble(5, checking);
            pstmt.setDouble(6, saving);
            pstmt.setString(7, address);
            pstmt.setString(8, Country);
            pstmt.executeUpdate();
            System.out.println("International Debit Account created");
            //send_mail_new_Account_International_Debit(email, card_num, get_code);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }



    public void create_credit_account(String name, String email, String address, double checking, double saving) throws NoSuchAlgorithmException {
        //Country
        Currency usa = Currency.getInstance("USD");
        String curr_code = usa.getCurrencyCode();
        // Read input scan
        Scanner scan = new Scanner(System.in);
        //Creating a KeyGenerator object Cryptography key
        KeyGenerator keyGen = KeyGenerator.getInstance("DES");

        //Creating a SecureRandom object
        SecureRandom secRandom = new SecureRandom();

        //Initializing the KeyGenerator
        keyGen.init(secRandom);

        //Creating/Generating a key
        Key key = keyGen.generateKey();
        String secure_code = key.toString();
        String get_code = secure_code.substring(28);
        // System.out.println(get_code);
        //create account details
        int card_num = secRandom.nextInt(11111);
        //Insert inputs into database Table (creating account)
        String read_data = "INSERT INTO InovCREDIT(NAME, EMAIL, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY) VALUES " +
                    "(?, ?, ?, ?, ?, ?, ?, ?)";
        try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(read_data)) {
            pstmt.setString(1, name);
            pstmt.setString(2, email);
            pstmt.setInt(3, card_num);
            pstmt.setString(4, get_code);
            pstmt.setDouble(5, checking);
            pstmt.setDouble(6, saving);
            pstmt.setString(7, address);
            pstmt.setString(8, curr_code);
            pstmt.executeUpdate();
            System.out.println("Credit Account created");
            //send_mail_new_Account_Credit(email, card_num, get_code);
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }


    public void deposit_checking_debit(int cardno, double deposit) throws SQLException {
        Statement state = connect().createStatement();
        // transaction processing
        String debit_data = "UPDATE InovDEBIT set CHECKING=CHECKING+? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_data);
        stat.setDouble(1, deposit);
        stat.setInt(2, cardno);
        stat.executeUpdate();// transaction complete
        System.out.println("Deposit successful");
        //send_mail_deposit_Checking(email, deposit);
    }


    public void deposit_saving_debit(int cardno, double deposit) throws SQLException {
        Statement state = connect().createStatement();
        // transaction processing
        String debit_data = "UPDATE InovDEBIT set SAVING=SAVING+? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_data);
        stat.setDouble(1, deposit);
        stat.setInt(2, cardno);
        stat.executeUpdate();// transaction complete
        System.out.println("Deposit successful");
        //send_mail_deposit_Saving(email, deposit);
    }

    public void deposit_checking_credit(int cardno, double deposit) throws SQLException {
        Statement state = connect().createStatement();
        // transaction processing
        String debit_data = "UPDATE InovCREDIT set CHECKING=CHECKING+? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_data);
        stat.setDouble(1, deposit);
        stat.setInt(2, cardno);
        stat.executeUpdate();// transaction complete
        System.out.println("Deposit successful");
        //send_mail_deposit_Checking(email, deposit);
    }

    public void deposit_saving_credit(int cardno, double deposit) throws SQLException {
        Statement state = connect().createStatement();
        // transaction processing
        String debit_data = "UPDATE InovCREDIT set SAVING=SAVING+? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_data);
        stat.setDouble(1, deposit);
        stat.setInt(2, cardno);
        stat.executeUpdate();// transaction complete
        System.out.println("Deposit successful");
        //send_mail_deposit_Saving(email, deposit);
    }


    public void withdraw_checking_Debit(int cardnum, double withdraw) throws SQLException {
        Statement state = connect().createStatement();
        // transaction processing
        String debit_data = "UPDATE InovDEBIT set CHECKING=CHECKING-? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_data);
        stat.setDouble(1, withdraw);
        stat.setInt(2, cardnum);
        stat.executeUpdate();
        System.out.println("Withdrawal successful");
    }

    public void withdraw_saving_Debit(int cardnum, double withdraw) throws SQLException {
        Statement state = connect().createStatement();
        // transaction processing
        String debit_data = "UPDATE InovDEBIT set SAVING=SAVING-? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_data);
        stat.setDouble(1, withdraw);
        stat.setInt(2, cardnum);
        stat.executeUpdate();
        System.out.println("Withdrawal successful");
    }

    public void withdraw_checking_Credit(int cardnum, double withdraw) throws SQLException {
        Statement state = connect().createStatement();
        // transaction processing
        String debit_data = "UPDATE InovCREDIT set CHECKING=CHECKING-? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_data);
        stat.setDouble(1, withdraw);
        stat.setInt(2, cardnum);
        stat.executeUpdate();
        System.out.println("Withdrawal successful");
    }

    public void withdraw_saving_Credit(int cardnum, double withdraw) throws SQLException {
        Statement state = connect().createStatement();
        // transaction processing
        String debit_data = "UPDATE InovCREDIT set SAVING=SAVING-? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_data);
        stat.setDouble(1, withdraw);
        stat.setInt(2, cardnum);
        stat.executeUpdate();
        System.out.println("Withdrawal successful");
    }

    // Debit
    public void send_money_debit(int cardcode, double amount, String recipient) throws SQLException {
        // collect valued amount to be sent to recipient (debit check)
        String debit_send = "UPDATE InovDEBIT set CHECKING=CHECKING-? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_send);
        stat.setDouble(1, amount);
        stat.setInt(2, cardcode);
        String debit_receive = "UPDATE InovDEBIT set CHECKING=CHECKING+? WHERE NAME=?";
        PreparedStatement stat2 = connect().prepareStatement(debit_receive);
        stat2.setDouble(1, amount);
        stat2.setString(2, recipient);
        System.out.println("Transfer processed");
        //send_mail_transaction(email, amount, name);
    }

    public void send_debit_to_credit(int cardcode, double amount, String recipient) throws SQLException {
        // collect valued amount to be sent to recipient (debit check)
        String debit_send2 = "UPDATE InovDEBIT set CHECKING=CHECKING-? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_send2 );
        stat.setDouble(1, amount);
        stat.setInt(2, cardcode);
        String debit_receive2 = "UPDATE InovCREDIT set CHECKING=CHECKING+? WHERE NAME=?";
        PreparedStatement stat2 = connect().prepareStatement(debit_receive2);
        stat2.setDouble(1, amount);
        stat2.setString(2, recipient);
        System.out.println("Transfer processed");
    }



    // Send Debit & Credit to International Debit account
    public  void credit_debit_to_international(String base, String convert, int cardcode, double amount, String recipient) throws SQLException, IOException {
        tran.Credit_Debit_currency_InternationalTransactions(base, convert, cardcode, amount, recipient);
    }
    // Credit
    public void send_money_credit(int cardcode, double amount, String recipient) throws SQLException {
        String retrieve = "UPDATE InovCREDIT set CHECKING=CHECKING-? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(retrieve);
        stat.setDouble(1, amount);
        stat.setInt(2, cardcode);
        String accept2 = "UPDATE InovCREDIT set CHECKING=CHECKING+? WHERE NAME=?";
        PreparedStatement stat2 = connect().prepareStatement(accept2);
        stat2.setDouble(1, amount);
        stat2.setString(2, recipient);
        stat.executeUpdate();
        stat2.executeUpdate();
        System.out.println("Transfer processed");
        //send_mail_transaction(email, amount, name);
    }



    public void send_credit_to_debit(int cardcode, double amount, String recipient) throws SQLException {
        // collect valued amount to be sent to recipient (debit check)
        String debit_send2 = "UPDATE InovCREDIT set CHECKING=CHECKING-? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(debit_send2 );
        stat.setDouble(1, amount);
        stat.setInt(2, cardcode);
        String debit_receive2 = "UPDATE InovDEBIT set CHECKING=CHECKING+? WHERE NAME=?";
        PreparedStatement stat2 = connect().prepareStatement(debit_receive2);
        stat2.setDouble(1, amount);
        stat2.setString(2, recipient);
        System.out.println("Transfer processed");
    }


    // Bank Statements
    public void debit_bank_statement(int cardcode) throws SQLException {
        // String debit = "SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM DEBITInov";
        Statement state = connect().createStatement();
        ResultSet retract_debit = state.executeQuery("SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM InovDEBIT WHERE CARDNUM=?");
        while (retract_debit.next()) {
            String account_name = retract_debit.getString("NAME");
            int card_num = retract_debit.getInt("CARDNUM");
            String card_code = retract_debit.getString("CARDCODE");
            double checking_balance = retract_debit.getDouble("CHECKING");
            double saving_balance = retract_debit.getDouble("SAVING");
            String address = retract_debit.getString("ADDRESS");
            String currency = retract_debit.getString("CURRENCY");
            System.out.println("Account Holder = " + account_name);
            System.out.println("Card Numbers =  " + card_num);
            System.out.println("Card Codes = " + card_code);
            System.out.println("Checking Balances = " + checking_balance);
            System.out.println("Savings Balances = " + saving_balance);
            System.out.println("Addresses = " + address);
            System.out.println("Currency = " + currency);
        }
    }

    public void credit_bank_statement(int cardcode) throws SQLException {
        // String debit = "SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM DEBITInov";
        Statement state = connect().createStatement();
        ResultSet retract_credit = state.executeQuery("SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM InovCREDIT WHERE CARDNUM=?");
        while (retract_credit.next()) {
            String account_name = retract_credit.getString("NAME");
            int card_num = retract_credit.getInt("CARDNUM");
            String card_code = retract_credit.getString("CARDCODE");
            double checking_balance = retract_credit.getDouble("CHECKING");
            double saving_balance = retract_credit.getDouble("SAVING");
            String address = retract_credit.getString("ADDRESS");
            String currency = retract_credit.getString("CURRENCY");
            System.out.println("Account Holder = " + account_name);
            System.out.println("Card Numbers =  " + card_num);
            System.out.println("Card Codes = " + card_code);
            System.out.println("Checking Balances = " + checking_balance);
            System.out.println("Savings Balances = " + saving_balance);
            System.out.println("Addresses = " + address);
            System.out.println("Currency = " + currency);
        }
    }

    public void International_Debit_bank_statement(int cardcode) throws SQLException {
        // String debit = "SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM DEBITInov";
        Statement state = connect().createStatement();
        ResultSet retract_credit = state.executeQuery("SELECT NAME, CARDNUM, CARDCODE, CHECKING, SAVING, ADDRESS, CURRENCY FROM InovInterDEBIT WHERE CARDNUM=?");
        while (retract_credit.next()) {
            String account_name = retract_credit.getString("NAME");
            int card_num = retract_credit.getInt("CARDNUM");
            String card_code = retract_credit.getString("CARDCODE");
            double checking_balance = retract_credit.getDouble("CHECKING");
            double saving_balance = retract_credit.getDouble("SAVING");
            String address = retract_credit.getString("ADDRESS");
            String currency = retract_credit.getString("CURRENCY");
            System.out.println("Account Holder = " + account_name);
            System.out.println("Card Numbers =  " + card_num);
            System.out.println("Card Codes = " + card_code);
            System.out.println("Checking Balances = " + checking_balance);
            System.out.println("Savings Balances = " + saving_balance);
            System.out.println("Addresses = " + address);
            System.out.println("Currency = " + currency);
        }
    }

    public void payment_processor(String Cardcode) throws SQLException {
        Scanner scan3 = new Scanner(System.in);
        double price = 20;
        System.out.println("Please select ?");
        System.out.println("1. Debit ");
        System.out.println("2. Credit ");
        String accnt_line = scan3.nextLine();
        if (accnt_line.equals("1")) {
            pay.getCard_Debit(Cardcode, price);
        }
        if (accnt_line.equals("2")) {
            pay.getCard_Credit(Cardcode, price);
        }
    }

    public void Currency_exchange(String base_curr, String convert_curr, int cardcode) throws SQLException, IOException {
        chan.Country_currency_CurrencyExchange(base_curr, convert_curr, cardcode);
    }

    public void International_debit_send(String base_curr, String Country_name, int cardcode, double amount, String name) throws SQLException, IOException {
        current.Country_currency_InternationalTransactions(base_curr, Country_name, cardcode, amount, name);
    }

    public void delete_debit_account(int cardnum) throws SQLException {
        bdms.delete_account_debit(cardnum);
    }
    public void delete_credit_account(int cardnum) throws SQLException {
        bdms.delete_account_credit(cardnum);
    }
    public void delete_International_debit_account(int cardnum) throws SQLException {
        bdms.delete_account_InternationalDebit(cardnum);
    }


    public static void send_mail_new_Account_Debit(String mail, int cardno, String cardcode) {
        // email ID of  Sender.
        String sender = "monetarytransatlantic@gmail.com";
        // using host as localhost
        String host = "204.14.73.237";
        // Getting system properties
        Properties properties = System.getProperties();
        // Setting up mail server
        properties.setProperty("mail.smtp.host", host);
        // creating session object to get properties
        Session session = Session.getDefaultInstance(properties);

        try {
            // MimeMessage object.
            MimeMessage message = new MimeMessage(session);
            // Set From Field: adding senders email to from field.
            message.setFrom(new InternetAddress(sender));
            // Set To Field: adding recipient's email to from field.
            message.addRecipient(Message.RecipientType.TO, new InternetAddress(mail));
            // Set Subject: subject of the email
            message.setSubject("Congrats on your new Account!!!");
            message.setText("\"Congrats on your new Debit Bank account!!! This " + cardno + " is your card number. This " + cardcode + " is your secured \" \\\n" +
                    "            \"card \" \\\n" +
                    "            \"code that will be used to secure your account. \"");
            Transport.send(message);
        } catch (MessagingException mex) {
            mex.printStackTrace();
        }
    }

    public static void send_mail_new_Account_Credit(String mail, int cardno, String cardcode) {
        // email ID of  Sender.
        String sender = "monetarytransatlantic@gmail.com";
        // using host as localhost
        String host = "127.0.0.1";
        // Getting system properties
        Properties properties = System.getProperties();
        // Setting up mail server
        properties.setProperty("mail.smtp.host", host);
        // creating session object to get properties
        Session session = Session.getDefaultInstance(properties);

        try {
            // MimeMessage object.
            MimeMessage message = new MimeMessage(session);
            // Set From Field: adding senders email to from field.
            message.setFrom(new InternetAddress(sender));
            // Set To Field: adding recipient's email to from field.
            message.addRecipient(Message.RecipientType.TO, new InternetAddress(mail));
            // Set Subject: subject of the email
            message.setSubject("Congrats on your new Account!!!");
            message.setText("\"Congrats on your new Credit Bank account!!! This " + cardno + " is your card number. This " + cardcode + " is your secured \" \\\n" +
                    "            \"card \" \\\n" +
                    "            \"code that will be used to secure your account. \"");
            Transport.send(message);
        } catch (MessagingException mex) {
            mex.printStackTrace();
        }
    }

    public static void send_mail_new_Account_International_Debit(String mail, int cardno, String cardcode) {
        // email ID of  Sender.
        String sender = "monetarytransatlantic@gmail.com";
        // using host as localhost
        String host = "172.16.29.25";
        // Getting system properties
        Properties properties = System.getProperties();
        // Setting up mail server
        properties.setProperty("mail.smtp.host", host);
        // creating session object to get properties
        Session session = Session.getDefaultInstance(properties);

        try {
            // MimeMessage object.
            MimeMessage message = new MimeMessage(session);
            // Set From Field: adding senders email to from field.
            message.setFrom(new InternetAddress(sender));
            // Set To Field: adding recipient's email to from field.
            message.addRecipient(Message.RecipientType.TO, new InternetAddress(mail));
            // Set Subject: subject of the email
            message.setSubject("Congrats on your new Account!!!");
            message.setText("\"Congrats on your new International Debit Bank account!!! This " + cardno + " is your card number. This " + cardcode + " is your secured \" \\\n" +
                    "            \"card \" \\\n" +
                    "            \"code that will be used to secure your account. \"");
            Transport.send(message);
        } catch (MessagingException mex) {
            mex.printStackTrace();
        }
    }

    public static void send_mail_transaction(String mail, double amount, String name) {
        // email ID of  Sender.
        String sender = "monetarytransatlantic@gmail.com";
        // using host as localhost
        String host = "127.0.0.1";
        // Getting system properties
        Properties properties = System.getProperties();
        // Setting up mail server
        properties.setProperty("mail.smtp.host", host);
        // creating session object to get properties
        Session session = Session.getDefaultInstance(properties);
        try {
            // MimeMessage object.
            MimeMessage message = new MimeMessage(session);
            // Set From Field: adding senders email to from field.
            message.setFrom(new InternetAddress(sender));
            // Set To Field: adding recipient's email to from field.
            message.addRecipient(Message.RecipientType.TO, new InternetAddress(mail));
            // Set Subject: subject of the email
            message.setSubject("Money Sent!!!");
            message.setText("You have received $ " + amount + " from " + name);
            Transport.send(message);
            Transport.send(message);
            System.out.println("Mail successfully sent");
        } catch (MessagingException mex) {
            mex.printStackTrace();
        }
    }

    public static void send_mail_International_transaction(String mail, double amount, String name, String Country) {
        // email ID of  Sender.
        String sender = "monetarytransatlantic@gmail.com";
        // using host as localhost
        String host = "127.0.0.1";
        // Getting system properties
        Properties properties = System.getProperties();
        // Setting up mail server
        properties.setProperty("mail.smtp.host", host);
        // creating session object to get properties
        Session session = Session.getDefaultInstance(properties);
        try {
            // MimeMessage object.
            MimeMessage message = new MimeMessage(session);
            // Set From Field: adding senders email to from field.
            message.setFrom(new InternetAddress(sender));
            // Set To Field: adding recipient's email to from field.
            message.addRecipient(Message.RecipientType.TO, new InternetAddress(mail));
            // Set Subject: subject of the email
            message.setSubject("Money Sent!!!");
            message.setText("You have received $ " + amount + " from " + name + "in " + Country);
            Transport.send(message);
            System.out.println("Mail successfully sent");
        } catch (MessagingException mex) {
            mex.printStackTrace();
        }
    }

    public static void send_mail_currency_exchange(String mail, String converted_Currency) {
        // email ID of  Sender.
        String sender = "monetarytransatlantic@gmail.com";
        // using host as localhost
        String host = "127.0.0.1";
        // Getting system properties
        Properties properties = System.getProperties();
        // Setting up mail server
        properties.setProperty("mail.smtp.host", host);
        // creating session object to get properties
        Session session = Session.getDefaultInstance(properties);
        try {
            // MimeMessage object.
            MimeMessage message = new MimeMessage(session);
            // Set From Field: adding senders email to from field.
            message.setFrom(new InternetAddress(sender));
            // Set To Field: adding recipient's email to from field.
            message.addRecipient(Message.RecipientType.TO, new InternetAddress(mail));
            // Set Subject: subject of the email
            message.setSubject("Converted Cash account");
            // set body of the email.
            message.setText("You have converted your account to this currency = " + converted_Currency);
            // Send email.
            Transport.send(message);
            System.out.println("Mail successfully sent");
        } catch (MessagingException mex) {
            mex.printStackTrace();
        }
    }


    public static void send_mail_deposit_Checking(String mail, double deposit) {
        // email ID of  Sender.
        String sender = "monetarytransatlantic@gmail.com";
        // using host as localhost
        String host = "127.0.0.1";
        // Getting system properties
        Properties properties = System.getProperties();
        // Setting up mail server
        properties.setProperty("mail.smtp.host", host);
        // creating session object to get properties
        Session session = Session.getDefaultInstance(properties);
        try {
            // MimeMessage object.
            MimeMessage message = new MimeMessage(session);
            // Set From Field: adding senders email to from field.
            message.setFrom(new InternetAddress(sender));
            // Set To Field: adding recipient's email to from field.
            message.addRecipient(Message.RecipientType.TO, new InternetAddress(mail));
            // Set Subject: subject of the email
            message.setSubject("Deposit");
            // set body of the email.
            message.setText("You have just deposited " + deposit + "into your checking account.");
            // Send email.
            Transport.send(message);
            System.out.println("Mail successfully sent");
        } catch (MessagingException mex) {
            mex.printStackTrace();
        }
    }

    public static void send_mail_deposit_Saving(String mail, double deposit) throws UnsupportedEncodingException {
        Properties props = new Properties();
        Session session = Session.getDefaultInstance(props, null);

        try {
            Message msg = new MimeMessage(session);
            msg.setFrom(new InternetAddress("monetarytransatlantic@gmail.com", "Inov inc"));
            msg.addRecipient(Message.RecipientType.TO,
                    new InternetAddress(mail, "User"));
            msg.setSubject("Your Example.com account has been activated");
            msg.setText("You just made a deposit of $" + deposit + "into your savings account");
            Transport.send(msg);
        } catch (MessagingException | UnsupportedEncodingException e) {
            System.out.println("email cant be processed");
        }
    }
}









