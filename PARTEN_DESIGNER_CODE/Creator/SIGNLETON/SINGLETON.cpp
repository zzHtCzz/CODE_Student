#include "iostream"
using namespace std;

class SINGLETON
{
    private :
    int value;
    static SINGLETON *s_instance;
    public:
    int getvalue(){
     return value;
    }
    void setvalue(int v)
    {
      value=v;
    }

    static SINGLETON *instance()
    {
        if(!s_instance) //nếu biến s_instance=null
        {
          s_instance=new SINGLETON;
          
        }
        return s_instance;
    }

};

SINGLETON *SINGLETON::s_instance=0; //KHOI TAO BAN DAU BANG 0


void a()
{
    SINGLETON::instance()->setvalue(0);
    cout<<SINGLETON::instance()->getvalue()<<endl;
}
void b()
{
    SINGLETON::instance()->setvalue(1);
    cout<<SINGLETON::instance()->getvalue()<<endl;
}
int main()
{
    a();
    b();
}