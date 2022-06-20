public class TimeFormatter {
    
    public static String formatDuration(int seconds) {
        String[] timeStrings = {"year", "day", "hour", "minute", "second"};
        int[] timeInts = {31536000, 86400, 3600, 60, 1};
        String answer = "";
        
        if(seconds == 0) return "now";
        
        int wordsNumber = 0;
        for(int index = 0; index < timeStrings.length; index++) {
            int amt = seconds / timeInts[index];
            if(amt == 0) timeStrings[index] = "";
            else {
                if(amt > 1) timeStrings[index] += "s";
                timeStrings[index] = amt + " " + timeStrings[index];
                wordsNumber++;
            }
            seconds = seconds % timeInts[index];
        }
        
        for(int index = 0; index < timeStrings.length; index++) {
            answer += timeStrings[index];
            
            if(!(timeStrings[index].equals(""))) {
                if(wordsNumber == 2) answer += " and ";
                else if(wordsNumber > 2) answer += ", ";
                wordsNumber--;
            }
        }
        return answer;
    }
}
