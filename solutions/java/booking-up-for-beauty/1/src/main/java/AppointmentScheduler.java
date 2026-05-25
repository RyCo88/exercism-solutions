import java.time.LocalDate;
import java.time.LocalDateTime;

class AppointmentScheduler {
    public LocalDateTime schedule(String appointmentDateDescription) {
        String[] parts = appointmentDateDescription.split(" ");
        String[] dateParts = parts[0].split("/");
        String[] timeParts = parts[1].split(":");

        int month = Integer.parseInt(dateParts[0]);
        int day = Integer.parseInt(dateParts[1]);
        int year = Integer.parseInt(dateParts[2]);
        
        int hour = Integer.parseInt(timeParts[0]);
        int minute = Integer.parseInt(timeParts[1]);
        int second = Integer.parseInt(timeParts[2]);

        return LocalDateTime.of(year, month, day, hour, minute, second);
    }

    public boolean hasPassed(LocalDateTime appointmentDate) {
        return appointmentDate.isBefore(LocalDateTime.now());
    }

    public boolean isAfternoonAppointment(LocalDateTime appointmentDate) {
        int hour = appointmentDate.getHour();
        return hour >= 12 && hour < 18;
    }

    public String getDescription(LocalDateTime appointmentDate) {
        String dayOfWeek = appointmentDate.getDayOfWeek().name();
        String formattedDay = dayOfWeek.charAt(0) + dayOfWeek.substring(1).toLowerCase();

        String month = appointmentDate.getMonth().name();
        String formattedMonth = month.charAt(0) + month.substring(1).toLowerCase();

        int hour = appointmentDate.getHour();
        String amPm = (hour < 12) ? "AM" : "PM";
        
        int hour12 = (hour % 12 == 0) ? 12 : (hour % 12);
        
        int min = appointmentDate.getMinute();
        String minuteStr = (min < 10) ? "0" + min : String.valueOf(min);

        return String.format("You have an appointment on %s, %s %d, %d, at %d:%s %s.", 
            formattedDay, formattedMonth, appointmentDate.getDayOfMonth(), 
            appointmentDate.getYear(), hour12, minuteStr, amPm);
    }

    public LocalDate getAnniversaryDate() {
        int currentYear = LocalDate.now().getYear();
        return LocalDate.of(currentYear, 9, 15);
    }
}
