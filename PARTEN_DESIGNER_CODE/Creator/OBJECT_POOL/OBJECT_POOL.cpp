#include <string>
#include <iostream>
#include <list>
class Resource
{
    int value;
    public:
        Resource()
        {
            value = 0;
        }
        void reset()
        {
            value = 0;
        }
        int getValue()
        {
            return value;
        }
        void setValue(int number)
        {
            value = number;
        }
};
/* Note, that this class is a singleton. */
class ObjectPool
{
    private:
        std::list<Resource*> resources;
        static ObjectPool* instance;
        ObjectPool() {}
    public:
       
        static ObjectPool* getInstance()
        {
            if (instance == 0)
            {
                instance = new ObjectPool;
            }
            return instance;
        }
       
        Resource* getResource()
        {
            if (resources.empty())//kiểm tra trong list có pt nào k
            {
                std::cout << "Creating new." << std::endl;
                return new Resource;
            }
            else
            {
                std::cout << "Reusing existing." << std::endl;
                Resource* resource = resources.front();//lấy phần trử đầu
                resources.pop_front();//xóa phganaf rử đầu trong list
                return resource;
            }
        }
       
        void returnResource(Resource* object)
        {
            object->reset();
            resources.push_back(object);//thêm lkaij vào list
        }
};
ObjectPool* ObjectPool::instance = 0;
int main()
{
    ObjectPool* pool = ObjectPool::getInstance();
    Resource* one;
    Resource* two;
    //tạo lấy Oject bên trong réource
    one = pool->getResource();
    one->setValue(10);
    std::cout << "one = " << one->getValue() << " [" << one << "]" << std::endl;
    two = pool->getResource();
    two->setValue(20);
    std::cout << "two = " << two->getValue() << " [" << two << "]" << std::endl;

    //trả lại vào lits
    pool->returnResource(one);
    pool->returnResource(two);
    /* Resources will be reused.
     * Notice that the value of both resources were reset back to zero.
     */
    //lấy ra kiểm tra kaij xem object có phải object đã sử dụng hay lkaf nó tạo mới (đã sử dụng)
    //kết quả thấy dịa chỉ nó k đổi=>object cũ đã được tạo
    one = pool->getResource();
    std::cout << "one = " << one->getValue() << " [" << one << "]" << std::endl;
    two = pool->getResource();
    std::cout << "two = " << two->getValue() << " [" << two << "]" << std::endl;

    return 0;
}