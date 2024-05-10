import java.io.*;
import java.util.*;

public class DayOne{
    public static void main(String[] args) {

        String filePath = "dayOneInput.txt";
        
        try {
            // initialise objects for reading from file
            FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String eachLine;
            int sum = 0;

            while((eachLine = bufferedReader.readLine()) != null){
                ArrayList<Integer> digits = new ArrayList<>(); // store digits on line

                for(int i=0; i < eachLine.length(); i++){
                    if(Character.isDigit(eachLine.charAt(i))){
                        digits.add(Character.getNumericValue(eachLine.charAt(i)));
                    }
                }

                sum += (digits.get(0)*10) + digits.get(digits.size() - 1);
            }

            bufferedReader.close();

            System.out.println(sum);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
}