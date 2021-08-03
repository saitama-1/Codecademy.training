# names of hurricanes
from typing import no_type_check_decorator


names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def udpate_damages(lst_o):
    M = 1000000
    B = 1000000000
    lst_u = []
    for str_d in lst_o:
        if str_d != "Damages not recorded":
            if str_d[-1] == 'M':
                lst_u.append(float(str_d[:-1]) * M)
            else:
                lst_u.append(float(str_d[:-1]) * B)
        else:
            lst_u.append(str_d)
    return lst_u


# print(udpate_damages(damages))
# print("========================")





# write your construct hurricane dictionary function here:
def construct_dict(names, months, years,max_sustained_winds, areas_affected, damages, deaths):
    lst_K = ["Name", "Month", "Year", "Max Sustained Wind", "Areas Affected", "Damage", "Deaths"]
    hurricanes = zip(names, months, years,max_sustained_winds, areas_affected, damages, deaths)
    lst_r_dict = []
    for h in hurricanes:
        dict = {k: v for k, v in zip(lst_K, h)}
        lst_r_dict.append(dict)
    # {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}
    
    names_t_r = zip(names, lst_r_dict)
    r_dict={k:v for k, v in names_t_r}
    return r_dict

cstruct_dict = {}
cstruct_dict = construct_dict(names, months, years,max_sustained_winds, areas_affected, damages, deaths)






# write your construct hurricane by year dictionary function here:
def construct_h_by_year(years, cstruct_dict):
    years_u = []
    tmp_dict = {}
    for y in years:
        if y not in years_u:
            years_u.append(y)
    
    for y in years_u:
        tmp_lst = []
        for r_dict in cstruct_dict.values():
            if r_dict["Year"] == y:
                tmp_lst.append(r_dict)
        tmp_dict.update({y: tmp_lst})
    return tmp_dict

tmp_dict = construct_h_by_year(years, cstruct_dict)
print(construct_h_by_year(years, cstruct_dict)[1932])    
print("\n")







# write your count affected areas function here:
def count_affected_areas(areas_affected):
    tmp_dict = {}
    uq_a_lst = []
    for l in areas_affected:
        for a in l:
            if a not in uq_a_lst:
                uq_a_lst.append(a)
    
    for area in uq_a_lst:
        count = 0
        for l in areas_affected:
            for a in l:
                if a == area:
                    count +=1
        tmp_dict.update({area:count})
    
    return tmp_dict

# print(count_affected_areas(areas_affected))
# print("===========================")
dct_areas_affected = count_affected_areas(areas_affected)



# write your find most affected area function here:

def most_affected_area(dct_areas_affected):
    max_v = list(dct_areas_affected.values())[0]
    max_k = list(dct_areas_affected.keys())[0]
    for k,v in dct_areas_affected.items():
        if v > max_v:
            max_v = v
            max_k = k
    return {max_k:max_v}
        
print(most_affected_area(dct_areas_affected))
print("\n")




# write your greatest number of deaths function here:
def greatest_n_of_deaths(names, deaths):
    n_to_d_zip = zip(names, deaths)
    n_to_d_lst = list(zip(names, deaths))
    n_to_d_dict = {n: d for n, d in n_to_d_zip}

    max_k = n_to_d_lst[0][0]
    max_v = n_to_d_lst[0][1]

    for k, v in n_to_d_dict.items():
        if v>max_v:
            max_v = v
            max_k = k
    return {max_k:max_v}

print(greatest_n_of_deaths(names, deaths))
print("\n")







# write your catgeorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def cat_mortality(names, deaths):
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}

    n_t_d_dict = {n:d for n, d in zip(names, deaths)}
    tmp_dict = [{},{},{},{},{},{}]
    for n, d in n_t_d_dict.items():
        if d<=0:
            tmp_dict[0].update({n:d})
        elif d<=100:
            tmp_dict[1].update({n:d})
        elif d<=500:
            tmp_dict[2].update({n:d})
        elif d<=10000:
            tmp_dict[3].update({n:d})
        elif d<=10000:
            tmp_dict[4].update({n:d})
        else:
            tmp_dict[5].update({n:d})
    for i in range(len(hurricanes_by_mortality)):
        hurricanes_by_mortality[i].append(tmp_dict[i])

    return hurricanes_by_mortality

print(cat_mortality(names, deaths))
print("\n")
        
    






# write your greatest damage function here:

def greatest_damage(names, damages):
    for i in range(len(damages)):
        if type(damages[i]) != float:        
            damages[i] = 0.0

    n_d_lst = list(zip(names, damages))
    max_d = n_d_lst[0][1]
    max_n = n_d_lst[0][0]
    for n, d in zip(names, damages):
        if d > max_d:
            max_d = d
            max_n = n

    return [max_n, max_d]


print(greatest_damage(names, udpate_damages(damages)))
print("\n")






# write your catgeorize by damage function here:



def cat_by_damage(names, damages):
    d_s = {0: 0,
            1: 100000000,
            2: 1000000000,
            3: 10000000000,
            4: 50000000000}

    for i in range(len(damages)):
        if type(damages[i]) != float:        
            damages[i] = 0.0
    
    hurricanes_by_damages = {0:[],1:[],2:[],3:[],4:[],5:[]}

    n_t_d_dict = {n:d for n, d in zip(names, damages)}
    tmp_dict = [{},{},{},{},{},{}]
    for n, d in n_t_d_dict.items():
        if d<=d_s[0]:
            tmp_dict[0].update({n:d})
        elif d<=d_s[1]:
            tmp_dict[1].update({n:d})
        elif d<=d_s[2]:
            tmp_dict[2].update({n:d})
        elif d<=d_s[3]:
            tmp_dict[3].update({n:d})
        elif d<=d_s[4]:
            tmp_dict[4].update({n:d})
        else:
            tmp_dict[5].update({n:d})
    for i in range(len(hurricanes_by_damages)):
        hurricanes_by_damages[i].append(tmp_dict[i])

    return hurricanes_by_damages

print(cat_by_damage(names, udpate_damages(damages)))