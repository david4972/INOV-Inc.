import java.io.IOException;
import java.sql.SQLException;
import java.util.Currency;

// access to all 70 countries for International transactions

public class Currencies {

    InternationalTransactions send = new InternationalTransactions();

    public void Country_currency_InternationalTransactions(String base_curr, String Country_name, int cardcode, double amount, String name) throws SQLException, IOException {
        // North America
        if (Country_name.equals("United States")){
            Currency usa = Currency.getInstance("USD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Canada")){
            Currency usa = Currency.getInstance("CAD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Mexico")){
            Currency usa = Currency.getInstance("MXN");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        // South America
        if (Country_name.equals("Brazil")){
            Currency usa = Currency.getInstance("BRL");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Argentina")){
            Currency usa = Currency.getInstance("ARS");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Chile")){
            Currency usa = Currency.getInstance("CLF");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Colombia")){
            Currency usa = Currency.getInstance("COU");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Peru")){
            Currency usa = Currency.getInstance("PEN");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Ecuador")){
            Currency usa = Currency.getInstance("USD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Uruguay")){
            Currency usa = Currency.getInstance("UYU");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Bolivia")){
            Currency usa = Currency.getInstance("BOB");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Paraguay")){
            Currency usa = Currency.getInstance("PYG");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Guyana")){
            Currency usa = Currency.getInstance("GYD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        //Europe
        if (Country_name.equals("Germany")){
            Currency usa = Currency.getInstance("EUR");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("United Kingdom")){
            Currency usa = Currency.getInstance("GBP");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("France")){
            Currency usa = Currency.getInstance("EUR");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Italy")){
            Currency usa = Currency.getInstance("EUR");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Russia")){
            Currency usa = Currency.getInstance("RUB");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Spain")){
            Currency usa = Currency.getInstance("EUR");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Netherlands")){
            Currency usa = Currency.getInstance("EUR");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Switzerland")){
            Currency usa = Currency.getInstance("CHF");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Poland")){
            Currency usa = Currency.getInstance("PLN");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Sweden")){
            Currency usa = Currency.getInstance("SEK");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        // Africa
        if (Country_name.equals("Nigeria")){
            Currency usa = Currency.getInstance("NGN");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("South Africa")){
            Currency usa = Currency.getInstance("ZAR");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Egypt")){
            Currency usa = Currency.getInstance("EGP");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Algeria")){
            Currency usa = Currency.getInstance("DZD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Morocco")){
            Currency usa = Currency.getInstance("MAD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Kenya")){
            Currency usa = Currency.getInstance("KES");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Ethiopia")){
            Currency usa = Currency.getInstance("ETB");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Ghana")){
            Currency usa = Currency.getInstance("GHS");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Angola")){
            Currency usa = Currency.getInstance("AOA");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Tanzania")){
            Currency usa = Currency.getInstance("TZS");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        // Asia
        if (Country_name.equals("China")){
            Currency usa = Currency.getInstance("CNY");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Japan")){
            Currency usa = Currency.getInstance("JPY");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("India")){
            Currency usa = Currency.getInstance("INR");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("South Korea")){
            Currency usa = Currency.getInstance("KRW");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Indonesia")){
            Currency usa = Currency.getInstance("IDR");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Taiwan")){
            Currency usa = Currency.getInstance("TWD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Thailand")){
            Currency usa = Currency.getInstance("THB");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("United Arab Emirates")){
            Currency usa = Currency.getInstance("AED");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Israel")){
            Currency usa = Currency.getInstance("ILS");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Philippines")){
            Currency usa = Currency.getInstance("PHP");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Hong Kong")){
            Currency usa = Currency.getInstance("HKD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Singapore")){
            Currency usa = Currency.getInstance("SGD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Malaysia")){
            Currency usa = Currency.getInstance("MYR");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Bangladesh")){
            Currency usa = Currency.getInstance("BDT");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Vietnam")){
            Currency usa = Currency.getInstance("VND");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        // Caribbean
        if (Country_name.equals("Antigua")){
            Currency usa = Currency.getInstance("XCD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Bahamas")){
            Currency usa = Currency.getInstance("BSD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Belize")){
            Currency usa = Currency.getInstance("BZD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Dominica")){
            Currency usa = Currency.getInstance("DOP");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Grenada")){
            Currency usa = Currency.getInstance("XCD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Jamaica")){
            Currency usa = Currency.getInstance("JMD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Puerto Rico")){
            Currency usa = Currency.getInstance("GYD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("St. Kitts and Nevis")){
            Currency usa = Currency.getInstance("XCD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("St. Lucia")){
            Currency usa = Currency.getInstance("XCD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("St. Vincent & Grenadines")){
            Currency usa = Currency.getInstance("XCD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Suriname")){
            Currency usa = Currency.getInstance("SRD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Trinidad & Tobago")){
            Currency usa = Currency.getInstance("TTD");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        // Central America
        if (Country_name.equals("Guatemala")){
            Currency usa = Currency.getInstance("GTQ");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Panama")){
            Currency usa = Currency.getInstance("PAB");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Costa Rica")){
            Currency usa = Currency.getInstance("CRC");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("El Salvador")){
            Currency usa = Currency.getInstance("PAB");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Honduras")){
            Currency usa = Currency.getInstance("HNL");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }
        if (Country_name.equals("Nicaragua")){
            Currency usa = Currency.getInstance("NIO");
            String curr_code = usa.getCurrencyCode();
            send.International_exchange(base_curr, curr_code, cardcode, amount, name);
        }

    }
}
