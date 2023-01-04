import java.net.*;
import java.io.*;
import java.nio.charset.*;
import com.google.gson.*;
//import yahoofinance.YahooFinance;
//import yahoofinance.quotes.fx.FxSymbols;
import java.net.URL;
import java.net.HttpURLConnection;
import java.math.*;
import java.sql.*;
//import java.util.Currency;
import java.util.Scanner;

public class exchangeApi {

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


    public void currency_exchange(String base_curr, String convert_curr, int cardcode) throws IOException, SQLException {
        Scanner scan = new Scanner(System.in);
        //Scanner scan2 = new Scanner(System.in);
        Character Line = '/';
        // Setting URL
        String url_str = "https://v6.exchangerate-api.com/v6/2816493d654f23cda23c4ccc/pair/";
        String join = base_curr.concat(String.valueOf(Line)).concat(convert_curr);
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
        BigDecimal req_result = jsonobj.get("conversion_rate").getAsBigDecimal();
        //double res = req_result.doubleValue();
        // Account
        System.out.println("Select account");
        System.out.println("1. Debit");
        System.out.println("2. Credit");
        System.out.println("3. International Debit");
        String read_accnt = scan.nextLine();
        if (read_accnt.equals("1")) {
            Currency_exchange_Debit(req_result, cardcode, convert_curr);
        }
        if (read_accnt.equals("2")) {
            Currency_exchange_Credit(req_result, cardcode, convert_curr);
        }
        if (read_accnt.equals("3")) {
            Currency_exchange_Debit_International(req_result, cardcode, convert_curr);
        }
    }


    public void Currency_exchange_Debit(BigDecimal rate_Debit, int cardcode, String convert_curr) throws SQLException, IOException {
        String debit_sql = "SELECT * FROM InovDEBIT WHERE CARDNUM=?";
        PreparedStatement e_debit_state = connect().prepareStatement(debit_sql);
        e_debit_state.setInt(1, cardcode);
        // Debit account check
        ResultSet retract_debit = e_debit_state.executeQuery();
        if (retract_debit.next()) {
            String credit_data = "UPDATE InovDEBIT set CHECKING=CHECKING*?, SAVING=SAVING*?, CURRENCY=? WHERE CARDNUM=?";
            PreparedStatement stat = connect().prepareStatement(credit_data);
            stat.setBigDecimal(1, rate_Debit);
            stat.setBigDecimal(2, rate_Debit);
            stat.setString(3, convert_curr);
            stat.setInt(4, cardcode);
            stat.executeUpdate();
            retract_debit.close(); // transaction complete
            //state.close();
            System.out.println("Conversion successful");
            //send_mail_deposit_Checking(email, deposit);

        }
    }

    public void Currency_exchange_Debit_International(BigDecimal rate_International_Debit, int cardcode, String convert_curr) throws SQLException, IOException {
        PreparedStatement exch_Debit_International = connect().prepareStatement("SELECT * FROM InovInterDEBIT WHERE CARDNUM=?");
        exch_Debit_International.setInt(1, cardcode);
        ResultSet retract_Debit_International = exch_Debit_International.executeQuery();
        if (retract_Debit_International.next()) {
            String credit_data = "UPDATE InovInterDEBIT set CHECKING=CHECKING*?, SAVING=SAVING*?, CURRENCY=? WHERE CARDNUM=?";
            PreparedStatement stat = connect().prepareStatement(credit_data);
            stat.setBigDecimal(1, rate_International_Debit);
            stat.setBigDecimal(2, rate_International_Debit);
            stat.setString(3, convert_curr);
            stat.setInt(4, cardcode);
            stat.executeUpdate();
            retract_Debit_International.close(); // transaction complete
            //state.close();
            System.out.println("Conversion successful");
            //send_mail_deposit_Checking(email, deposit);

        }
    }


    public void Currency_exchange_Credit(BigDecimal rate_Credit, int cardcode, String convert_curr) throws SQLException, IOException {
        PreparedStatement stat2 = connect().prepareStatement("SELECT * FROM InovCREDIT WHERE CARDNUM=?");
        stat2.setInt(1, cardcode);
        ResultSet retract_credit = stat2.executeQuery();
        if (retract_credit.next()) {
            String credit_data = "UPDATE InovCREDIT set CHECKING=CHECKING*?, SAVING=SAVING*?, CURRENCY=? WHERE CARDNUM=?";
            PreparedStatement stat = connect().prepareStatement(credit_data);
            stat.setBigDecimal(1, rate_Credit);
            stat.setBigDecimal(2, rate_Credit);
            stat.setString(3, convert_curr);
            stat.setInt(4, cardcode);
            stat.executeUpdate();
            retract_credit.close(); // transaction complete
            //state.close();
            System.out.println("Conversion successful");
            //send_mail_deposit_Checking(email, deposit);

        }
    }
}




