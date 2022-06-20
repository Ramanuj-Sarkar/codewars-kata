public class HexToRGB {
  
  public static int[] hexStringToRGB(String hex) {
    String newhex = hex.toLowerCase().substring(1);
    int number = 0;
    int[] answers = {0, 0, 0};
    int whichAnswer = 0;
    
    for(int digit = 0; digit < newhex.length(); digit++) {
      switch(newhex.charAt(digit)) {
        case '0': number += 0;break;
        case '1': number += 1;break;
        case '2': number += 2;break;
        case '3': number += 3;break;
        case '4': number += 4;break;
        case '5': number += 5;break;
        case '6': number += 6;break;
        case '7': number += 7;break;
        case '8': number += 8;break;
        case '9': number += 9;break;
        case 'a': number += 10;break;
        case 'b': number += 11;break;
        case 'c': number += 12;break;
        case 'd': number += 13;break;
        case 'e': number += 14;break;
        case 'f': number += 15;break;
      }
      switch(digit % 2)
      {
        case 0:number *= 16;break;
        case 1:
          answers[whichAnswer] = number;
          whichAnswer++;
          number = 0;
      }
    }
    return answers;
  }
}
