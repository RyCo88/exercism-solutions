public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        int check = speed;
        if (check < 5) {
            return check * 221.0;     
        }
        else if (check > 4 && check < 9) {
            return check * 221 * 0.9;
        }
        else if (check == 9) {
            return check * 221 * 0.8;
        }
        else {
            return check * 221 * .77;
        }
    }

    public int workingItemsPerMinute(int speed) {
        double productRate = productionRatePerHour(speed) / 60;
        int itWorks = (int) productRate;
        return itWorks;
    }
}
