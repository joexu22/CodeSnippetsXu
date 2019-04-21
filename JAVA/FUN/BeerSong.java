public class BeerSong {
    // TODO: look into event driven programming
    public static void main(String[] args) {
        int beerNum = 99;
        String word = "bottles";

        if (beerNum == 1) {
            word = "bottle"; // singular bottle instead of bottles
        }

        while (beerNum > 0) {

            System.out.println(beerNum + " " + word + " of beer on the wall");
            System.out.println(beerNum + " " + word + " of beer.");
            System.out.println("Take one down.");
            System.out.println("Pass it around.");

            beerNum = beerNum - 1;
            if (beerNum == 1) {
                word = "bottle"; // This part of the code is repeated, come up with solution that doesn't repeat
                                 // this
            }

            if (beerNum > 0) {
                System.out.println(beerNum + " " + word + " of beer on the wall.");
            } else {
                System.out.println("No more bottles of beer on the wall.");
            }
        }
    }
}