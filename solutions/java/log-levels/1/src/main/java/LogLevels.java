public class LogLevels {
    
    public static String message(String logLine) {
        String newLine;
        newLine = logLine.substring(logLine.indexOf(":") + 1);
        newLine = newLine.trim();
        
        return newLine;
    }

    public static String logLevel(String logLine) {
        String newLevel;
        newLevel = logLine.substring(logLine.indexOf("[") + 1, logLine.indexOf("]"));
        return newLevel.toLowerCase();
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
