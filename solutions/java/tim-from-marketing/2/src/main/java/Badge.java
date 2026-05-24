class Badge {
    public String print(Integer id, String name, String department) {
        String departmentFormat;
        if (department == null) {
            departmentFormat = "OWNER";
        } else {
            departmentFormat = department.toUpperCase();
        }

        if (id == null) {
            String badge = name + " - " + departmentFormat;
            return badge;
        } else {
            String badge = "[" + id + "] - " + name + " - " +departmentFormat;
            return badge;
        }
    }
}
