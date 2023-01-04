import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.sql.*;
import java.util.Scanner;

public class SendDebitCreditInter {
    public static Connection connect() {
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

    public void International_exchange(String base_curr, String convert_curr, int cardcode, double amount, String name) throws IOException, SQLException {
        Scanner scan3 = new Scanner(System.in);
        Character Line = '/';
        Character Line2 = '/';
        // Setting URL
        String url_str = "https://v6.exchangerate-api.com/v6/2816493d654f23cda23c4ccc/pair/";
        String join = base_curr.concat(String.valueOf(Line)).concat(convert_curr).concat(String.valueOf(Line2)).concat(String.valueOf(amount));
        String encodeStr = URLEncoder.encode(join, StandardCharsets.UTF_8.name());
        String combine = url_str + encodeStr;
        // Making Request
        URL url = new URL(combine);
        HttpURLConnection request = (HttpURLConnection) url.openConnection();
        request.connect();

        // Convert to JSON
        JsonParser jp = new JsonParser();
        JsonElement root = jp.parse(new InputStreamReader((InputStream) request.getContent()));
        JsonObject jsonobj = root.getAsJsonObject();

        // Accessing object
        BigDecimal req_result = jsonobj.get("conversion_result").getAsBigDecimal();
        // String res = Double.toString(req_result);
        double res = req_result.doubleValue();
        System.out.println("Please select ?");
        System.out.println("1. Debit ");
        System.out.println("2. Credit ");
        String accnt_line = scan3.nextLine();
        if (accnt_line.equals("1")) {
            send_debit_to_international(cardcode, res, name, convert_curr);
        }
        if (accnt_line.equals("2")) {
            send_credit_to_international(cardcode, res, name, convert_curr);
        }
    }

    // send from Debit to International Debit account
    public void send_debit_to_international(int cardcode, double amount, String recipient, String Country) throws SQLException {
        // collect valued amount to be sent to recipient (debit check)
            String retrieve = "UPDATE InovDEBIT set CHECKING=CHECKING-? WHERE CARDNUM=?";
            PreparedStatement stat = connect().prepareStatement(retrieve);
            stat.setDouble(1, amount);
            stat.setInt(2, cardcode);
            String accept = "UPDATE InovInterDEBIT set CHECKING=CHECKING+?, CURRENCY=? WHERE NAME=?";
            PreparedStatement stat2 = connect().prepareStatement(accept);
            stat2.setDouble(1, amount);
            stat2.setString(2, Country);
            stat2.setString(3, recipient);
            stat.executeUpdate();
            stat2.executeUpdate();
            System.out.println("Transfer processed");
    }

    // send from Credit to International Debit account
    public void send_credit_to_international(int cardcode, double amount, String recipient, String Country) throws SQLException {
        // collect valued amount to be sent to recipient (debit check)
        String retrieve = "UPDATE InovCREDIT set CHECKING=CHECKING-? WHERE CARDNUM=?";
        PreparedStatement stat = connect().prepareStatement(retrieve);
        stat.setDouble(1, amount);
        stat.setInt(2, cardcode);
        String accept = "UPDATE InovInterDEBIT set CHECKING=CHECKING+?, CURRENCY=? WHERE NAME=?";
        PreparedStatement stat2 = connect().prepareStatement(accept);
        stat2.setDouble(1, amount);
        stat2.setString(2, Country);
        stat2.setString(3, recipient);
        stat.executeUpdate();
        stat2.executeUpdate();
        System.out.println("Transfer processed");
        //send_mail_International_transaction(email, amount, name, Country);
        }
    }
