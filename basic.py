#---------------CONTIUE-STATE-------------

#check condition
weather_is_hot = 1; shark_warning = 0
if(weather_is_hot == 1) and \
	(shark_warning == 0):
		print('Pass')

print('''<bean id="IPM" class="com.taobao.tddl.jdbc.group.TGroupDataSource" init-method="init">
    <property name="appName" value="TMALL_AUCTION_APP" />
    <property name="dbGroupKey" value="TMALL_AUCTION_GROUP"/>
</bean>''')

varA, varB, varC = (1, 'str', 2.8)
print(varA, varB, varC)

#--------------------MODULE------------------

import simple_module

person = simple_module.Person(('Chris', 'Xu'))
person.sayHello()

simple_module.sayGoodBye()

print(simple_module.globalVar)

print(simple_module.__doc__)

print(person.__doc__)

#----------------------VARIABLES--------------------

x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)

#--------------------MEMORY-MANAGE-----------------

