package hackerrank.java;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.security.Permission;

public class Reflactions
{

    public static void main(String[] args) throws Exception
    {
        Do_Not_Terminate.forbidExit();

        try
        {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int num = Integer.parseInt(br.readLine().trim());
            Object o = null;// Must be used to hold the reference of the instance of the class
                     // Solution.Inner.Private

            Inner inner = new Inner();
            for (Constructor<?> ctor : Inner.Private.class.getDeclaredConstructors()) {
                ctor.setAccessible(true);
                o = ctor.newInstance(inner);
            }
            
            for (Method method : Inner.Private.class.getDeclaredMethods())
            {
                method.setAccessible(true);
                System.out.println(num + " is " + method.invoke(o, num));
                break;
            }
            
            System.out.println("An instance of class: " + o.getClass().getCanonicalName() + " has been created");

        }// end of try

        catch(Do_Not_Terminate.ExitTrappedException e)
        {
            System.out.println("Unsuccessful Termination!!");
        }
    }// end of main

    static class Inner
    {
        private class Private
        {
            private String powerof2(int num)
            {
                return ((num & num - 1) == 0) ? "power of 2" : "not a power of 2";
            }
        }
    }// end of Inner

}// end of Solution

class Do_Not_Terminate
{

    public static class ExitTrappedException extends SecurityException
    {

        private static final long serialVersionUID = 1L;
    }

    public static void forbidExit()
    {
        final SecurityManager securityManager = new SecurityManager() {
            @Override
            public void checkPermission(Permission permission)
            {
                if(permission.getName().contains("exitVM"))
                {
                    throw new ExitTrappedException();
                }
            }
        };
        System.setSecurityManager(securityManager);
    }
}
