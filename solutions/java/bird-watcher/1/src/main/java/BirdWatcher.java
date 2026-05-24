
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public static int[] getLastWeek() {
        return new int[] {0,2,5,3,7,8,4};
    }

    public int getToday() {
        return birdsPerDay[birdsPerDay.length - 1];
    }

    public void incrementTodaysCount() {
        birdsPerDay[birdsPerDay.length - 1] ++;
    }

    public boolean hasDayWithoutBirds() {
        for (int noBirds: birdsPerDay) {
            if (noBirds == 0) {
                return true;
            }
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int count = 0;

        if (numberOfDays > 7) {
            for (int i = 0; i < 7; i++) {
                count += birdsPerDay[i];
            }
            return count;
        }
        
        for (int i = 0; i < numberOfDays; i++) {
            count += birdsPerDay[i];
        }
        return count;
    }

    public int getBusyDays() {
        int busyDays = 0;
        for (int birds: birdsPerDay) {
            if (birds >= 5) {
                busyDays ++;
            }
        }
        return busyDays;
    }
}
