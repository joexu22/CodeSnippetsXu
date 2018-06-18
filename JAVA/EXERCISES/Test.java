class Test
{
    public static void main(String[] args)
    {
        Bicycle my_bike = new Bicycle();
        System.out.println("Testing, Testing, Testing");
        my_bike.printStates();
        my_bike.changeCadence(35);
        my_bike.changeGear(2);
        my_bike.speedUp(20);
        my_bike.printStates();
    }
}