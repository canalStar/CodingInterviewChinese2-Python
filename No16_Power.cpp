class Solution {
    
public: bool g_InavlidInput = false;    //定义全局变量，判断是否有非法输入，如0的负次幂

public:
    double Power(double base, int exponent) {
        g_InavlidInput = false;
        if(equal(base,0.0)&& exponent<0)
        {
            g_InavlidInput = true;
            return 0.0;
        }
        
        unsigned int absExponent = (unsigned int)(exponent);
        if(exponent < 0)
            absExponent = (unsigned int)(-exponent);
        
        double result = PowerWithUnsignedExponent(base, exponent);
        if (exponent < 0)
            result = 1.0 / result;
        return result;
    
    }
public:
    double PowerWithUnsignedExponent(double base, unsigned int exponent)
    {
        if(exponent == 0)
            return 1;
        if(exponent == 1)
            return base;
        double result = base;
        for(int i = 2; i <= exponent; i << 1)
            result *= result;
        if(exponent & 0x1 == 1)
            result *= base;
        return result;
    }
public:
    bool equal(double num1, double num2)
    {
        if((num1 - num2) > -0.0000001 && (num1 - num2) < 0.0000001)
            return true;        
        else
            return false;        
    }
}