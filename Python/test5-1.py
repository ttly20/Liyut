#This program is used for unit conversion
# - - codeing:utf-8 - -

#Size Conversion
class area :
    #Definition of basic properties
    km2 = 0  #Square kilometers
    ha = 0  #Square hectares
    acre = 0  #Square acre
    mile2 = 0  #Square miles
    m2 = 0  #sqm
    ft2 = 0  #sqft
    in2 = 0  #Square inch
    cm2 = 0  #Cm

    #Definition function:In terms of square kilometers hectares
    def km2ha(km2):
        return km2 * 100

    #Definition function:In terms of square kilomerers acres
    def km2acre(km2):
        return km2 * 247.1

    #Definition function:In terms of square miles square kilometers
    def km2mile2(km2):
        return km2 * 0.386

    #Definition function:Interms of square kilometers
    def km2m2(km2):
        return km2 * 247.1*4047

    #Definition function:Square kilometers in terms of square feet
    def km2ft2(km2):
        return km2*247.1*4047*10.764

    #Definition function:In terms of square kilometers Britain
    def km2in2(km2):
        return km2*247.1*4047*10.764*0.006944

    #Definition function:Square area in terms of square centimeters
    def km2cm2(km2):
        return km2*247.1*4047*10.764*0.006944*6.452

    #Definition function:Conversion kilometers square hectares
    def hakm2(ha):
        return ha/100

    #Definition function:Conversion square acre square hectares
    def haacre(ha):
        return ha*2.471

    #Definition function:In terms of square miles square hectares
    def hamile2(ha):
        return ha*259

    #Definition function:Hectare square meters conversion
    def ham2(ha):
        return ha*10000

    #Definition function:Square hectares conversion sqft
    def haft2(ha):
        return ha*107639.1

    #Definition function:Square hectares square inches conversion
    def hain2(ha):
        return ha*15500030

    #Definition function:Conversion cm square hectares
    def hacm2(ha):
        return ha*100000000

    #Definition function:Acre square kilometers Conversion
    def acrekm2(acre):
        return acre*(4.047*10-3)

    #Definition function:Conversion square acre square hectares
    def acreha(acre):
        return acre*0.4047

    #Definition function:Conversion square acre square miles
    def acremile2(acre):
        return acre*0.0016

    #Definition function:Conversion sqft Acres
    def acreft2(acre):
        return acre*43559.98

    #Definition function:Acre square inches conversion
    def acrein2(acre):
        return acre*42726365.86

    #Definition function:Conversion are square meters
    def acrem2(acre):
        return acre*4046.85

    #Definition function:Acre square centimeter conversion
    def acrecm2(acre):
        return acre*40468544.81

    #Definition function:In terms of square feet square kilometers
    def mile2km2(mile2):
        return mile2*2.59

    #Definition function:In terms of square feet square hectares
    def mile2ha(mile2):
        return mile2*259

    #Definition function:In terms of square feet square acres
    def mile2acre(mile2):
        return mile2*640

    #Definition funcion:In terms of square feet square feet
    def mile2ft2(mile2):
        return mile2*27878395.93

    #Definition function:Square-foot square inches conversion
    def mile2in2(mile2):
        return mile2*4014488909.93

    #Definition function:In terms of square meters square feet
    def mile2m2(mile2):
        return mile2*2589987.93

    #Definition function:Cm square foot conversion
    def mile2cm2(mile2):
        return mile2*25899878322.4

    #Definition function:In terms of square feet square kilometers
    def ft2km2(ft2):
        return ft2*0.000000092903

    #Definition function:In terms of square feet square hectares
    def ft2ha(ft2):
        return ft2*0.0000092903

    #Definition function:Conversion sqft Acres
    def ft2acre(ft2):
        return ft2*0.000023

    #Definition function:Square-foot square inches conversion
    def ft2in2(ft2):
        return ft2*144

    #Definition function:In terms of square meters square feet
    def ft2m2(ft2):
        return ft2*0.0929

    #definition function:Cm square foot conversion
    def ft2cm2(ft2):
        return ft2*929.03

    #Definition function:Square inches conversion square
    def in2km2(in2):
        return in2*0.000000000645

    #Definition function:Square inches conversion square hectares
    def in2ha(in2):
        return in2*0.000000064516

    #Definition function:Acre square inches conversion
    def in2acre(in2):
        return in2*0.0000001594

    #Definition function:Square inches conversion sqft
    def in2ft2(in2):
        return in2*0.0069

    #Definition function:In terms of square meters square inch
    def in2m2(in2):
        return in2*0.000645

    #Definition funcion:In terms of suqare inches cm
    def in2cm2(in2):
        return in2*6.4516

    #Definition function:Conversion square kilometers
    def m2km2(m2):
        return m2*0.0000001

    #Definition function:Conversion square hectares
    def m2ha(m2):
        return m2*0.0001

    #Definition function:Conversion acre square meters
    def m2acre(m2):
        return m2*0.000247

    #Definition function:In terms square meters square miles
    def m2mile2(m2):
        return m2*0.0000003861

    #Definition function:Sqm conversion sqft
    def m2ft2(m2):
        return m2*10.7639

    #Definition function:M2 square inches conversion
    def m2in2(m2):
        return m2*1550

    #Definition function:Conversion square cm
    def m2cm2(m2):
        return m2*10000

    #Definition function:Cm in terms of square kilometers
    def cm2km2(cm2):
        return cm2*0.0000000001

    #Definition function:Cm in terms of hectares
    def cm2ha(cm2):
        return cm2*0.00000001

    #Definition function:Cm in terms of acres
    def cm2acre(cm2):
        return cm2*0.000000024710550000000004

    #Definition function:Cm in terms of square miles
    def cm2mile2(cm2):
        return cm2*0.00000000003861022

    #Definition function:Cm in terms of square feet
    def cm2ft2(cm2):
        return cm2*0.0011

    #Definition function:Cm square inches conversion
    def cm2in2(cm2):
        return cm2*0.155

    #Definition function:Cm in terms of square meters
    def cm2m2(cm2):
        return cm2*0.0001

    #Definition function:Construction method
    def conversion(self):
        print('------This procedure is used in terms of area------')
        print('*Please select the way in terms of*')
        print('1.km2 --> ha  2.km2 -->acre  3.km2 -->mile2  4.km2 -->ft2\n5.km2 -->in2  6.km2 -->m2  7.km2 -->cm2  8.ha -->km2\n9.ha -->acre  10.ha -->mile2  11.ha -->ft2  12.ha -->in2\n13.ha -->m2  14.ha -->cm2  15.acre -->km2  16.acre -->ha\n17.acre -->mile2  18.acre -->ft2  19.acre -->in2  20.acre -->in2\n21.acre -->m2  22.acre -->cm2  23.mile2 -->km2  24.mile2 -->ha\n25.mile2 -->ft2  26.mile2 -->in2  27.mile2 -->m2  28.mile2 -->cm2\n29.ft2 -->km2  30.ft2 -->ha  31.ft2 -->acre  32.ft2 -->mile2\n33.ft2 -->in2  34.ft2 -->m2  35.ft2 -->cm2  36.in2 -->km2\n37.in2 -->ha  38.in2 -->acre  39.in2 -->mile2  40.in2 -->ft2\n41.in2 -->m2  42.in2 -->cm2  43.m2 -->km2  44.m2 -->ha\n45.m2 -->acre  46.m2 -->mile2  47.m2 -->ft2  48.m2 -->in2\n49.cm2 -->km2  50.cm2 -->ha  51.cm2 -->acre  52.cm2 -->mile2\n53.cm2 -->ft2  54.cm2 -->in2')
        print('***********************************')
        option = input('Please select:')
        value = input('Please enter a value:')
        if option == 1:
            print('%d square kilometers is equal to %d square hectares.'% (value,self.km2ha(value)))
        elif option == 2:
            print('%d square kilometers is equal to %d acres.'% (value,self.km2acre(value)))
        elif option == 3:
            print('%d square kilometers is equal to %d square miles.'% (value,self.km2mile2(value)))
        elif option == 4:
            print('%d square kilometers is equal to %d square feet.'% (value,self.km2ft2(value)))
        elif option == 5:
            print('%d square kilometers is equal to %d square inches.'% (value,self.km2in2(value)))
        elif option == 6:
            print('%d square kilometers is equal to %d square meters.'% (value,self.km2m2(value)))
        elif option == 7:
            print('%d square kilometers is equal to %d square centimeters.'% (value,self.km2cm2(value)))
        elif option == 8:
            print('%d hectares is equal to %d square kilometers.'% (value,self.hakm2(value)))
        elif option == 9:
            print('%d hectares is equal to %d acres.'% (value,self.haacre(value)))
        elif option == 10:
            print('%d hectares is equal to %d square miles.'% (value,self.hamile2(value)))
        elif option == 11:
            print('%d hectares is equal to %d square feet.'% (value,self.haft2(value)))
        elif option == 12:
            print('%d hectares is equal to %d square inches.'% (value,self.hain2(value)))
        elif option == 13:
            print('%d hectares is equal to %d square meters.'% (value,self.ham2(value)))
        elif option == 14:
            print('%d hectares is equal to %d square centimeters.'% (value,self.hacm2(value)))
        elif option == 15:
            print('%d acres is equal to %d square kilometers.'% (value,self.acrekm2(value)))
        elif option == 16:
            print('%d acres is equal to %d hectares.'% (value,self.acreha(value)))
        elif option == 17:
            print('%d acres is equal to %d square miles.'% (value,self.acremile2(value)))
        elif option == 18:
            print('%d acres is equal to %d square feet.'% (value,self.acreft2(value)))
        elif option == 19:
            print('%d acres is equal to %d square inches.'% (value,self.acrein2(value)))
        elif option == 20:
            print('%d acres is equal to %d hectares.'% (value,self.acreha(value)))
        elif option == 21:
            print('%d acres is equal to %d square meters.'% (value,self.acrem2(value)))
        elif option == 22:
            print('%d acres is equal to %d square centimeters.'% (value,self.acrecm2(value)))
        elif option == 23:
            print('%d square miles is equal to %d square kilometers.'% (value,self.mile2km2(value)))
        elif option == 24:
            print('%d square miles is equal to %d hectares.'% (value,self.mile2ha(value)))
        elif option == 25:
            print('%d square miles is equal to %d square feet.'% (value,self.mile2ft2(value)))
        elif option == 26:
            print('%d square miles is equal to %d square inches.'% (value,self.mile2in2(value)))
        elif option == 27:
            print('%d square miles is equal to %d square meters.'% (value,self.mile2m2(value)))
        elif option == 28:
            print('%d square miles is equal to %d square centimeters.'% (value,self.mile2cm2(value)))
        elif option == 29:
            print('%d square feet is equal to %d square kilometers.'% (value,self.ft2km2(value)))
        elif option == 30:
            print('%d square feet is equal to %d hectares.'% (value,self.ft2ha(value)))
        elif option == 31:
            print('%d square feet is equal to %d acres.'% (value,self.ft2acre(value)))
        elif option == 32:
            print('%d square feet is equal to %d square miles.'% (value,self.ft2mile2(value)))
        elif option == 33:
            print('%d square feet is equal to %d square inches.'% (value,self.ft2in2(value)))
        elif option == 34:
            print('%d square feet is equal to %d square meters.'% (value,self.ft2m2(value)))
        elif option == 35:
            print('%d square feet is equal to %d square centimeters.'% (value,self.ft2cm2(value)))
        elif option == 36:
            print('%d square inches is equal to %d square kilometers.'% (value,self.in2km2(value)))
        elif option == 37:
            print('%d square inches is equal to %d hectares.'% (value,self.in2ha(value)))
        elif option == 38:
            print('%d square inches is equal to %d acres.'% (value,self.in2acre(value)))
        elif option == 39:
            print('%d square inches is equal to %d square miles.'% (value,self.in2mile2(value)))
        elif option == 40:
            print('%d square inches is equal to %d square feet.'% (value,self.in2ft2(value)))
        elif option == 41:
            print('%d square inches is equal to %d square meters.'% (value,self.in2m2(value)))
        elif option == 42:
            print('%d square inches is equal to %d square centimeters.'% (value,self.in2cm2(value)))
        elif option == 43:
            print('%d square meters is equal to %d square kilometers.'% (value,self.m2km2(value)))
        elif option == 44:
            print('%d square meters is equal to %d hectares.'% (value,self.m2ha(value)))
        elif option == 45:
            print('%d square meters is equal to %d acres.'% (value,self.m2acre(value)))
        elif option == 46:
            print('%d square meters is equal to %d square miles.'% (value,self.m2mile2(value)))
        elif option == 47:
            print('%d square meters is equal to %d square feet.'% (value,self.m2ft2(value)))
        elif option == 48:
            print('%d square meters is equal to %d squar inches.'% (value,self.m2in2(value)))
        elif option == 49:
            print('%d square centimeters is equal to %d squar kilometers.'% (value,self.cm2km2(value)))
        elif option == 50:
            print('%d square centimeters is equal to %d squar hectares.'% (value,self.cm2ha(value)))
        elif option == 51:
            print('%d square centimeters is equal to %d acres.'% (value,self.cm2acre(value)))
        elif option == 52:
            print('%d square centimeters is equal to %d squar miles.'% (value,self.cm2mile2(value)))
        elif option == 53:
            print('%d square centimeters is equal to %d squar feet.'% (value,self.cm2ft2(value)))
        elif option == 54:
            print('%d square centimeters is equal to %d squar inches.'% (value,self.cm2in2(value)))
        else:
            print('Input error')
        return 0
x = area()
x.conversion()
