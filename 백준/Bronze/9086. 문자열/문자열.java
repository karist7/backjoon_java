import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = "";
        int n=Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            str = br.readLine();
            bw.write(String.format("%c%c\n",str.charAt(0),str.charAt(str.length()-1)));
        }

        bw.close();


    }
}