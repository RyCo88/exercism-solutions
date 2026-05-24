public class JedliksToyCar {

    private int metersDriven = 0;
    private int batteryLevel = 100;
    
    public static JedliksToyCar buy() {        
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + metersDriven + " meters";
    }

    public String batteryDisplay() {
        if (batteryLevel == 0) {
            return "Battery empty";
        } else {
            return "Battery at " + batteryLevel + "%";
        }
    }

    public void drive() {
        if (batteryLevel == 0) {
            batteryLevel = 0;
        } else {
            metersDriven += 20;
            batteryLevel -= 1;
        }
    }
}
