public class Lasagna {
    public int expectedMinutesInOven() {
        return 40;
    }
    public int remainingMinutesInOven(int minutesInOven) {
        Lasagna lasagna = new Lasagna();
        return lasagna.expectedMinutesInOven() - minutesInOven;
    }
    public int preparationTimeInMinutes(int numberOfLayers) {
        return numberOfLayers * 2;
    }
    public int totalTimeInMinutes(int numberOfLayers, int minutesInOven) {
        return numberOfLayers * 2 + minutesInOven;
    }
}
