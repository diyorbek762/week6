
def calculate_price_per_ticket(event_tuple):
    price_per_ticket=(event_tuple[3]/event_tuple[2])
    
    return price_per_ticket




def find_top_earning_event(events):
    unique_list=[]
    for event_name in events:
        unique_list.append((event_name[0], event_name[3]))

    unique_list.sort()
    
    sorted_list=[]
    for id, revenue in unique_list:
        sorted_list.append((-revenue, id))
    sorted_list.sort()

    top_earning_list=[]
    for neg_reveue, id in sorted_list:
        top_earning_list.append((id, -neg_reveue))
    return top_earning_list[0][0]


def get_events_by_artist(events, artist_name):
    search_by_artist_list=[]
    for event in events:
        if event[1]==artist_name:
            search_by_artist_list.append((event[0]))
    
    search_by_artist_list.sort()
    return search_by_artist_list


def get_artist_sales_summary(events):
    unique_list=[]
    full_list_of_ticket=[]
    for event in events:
        if event[1] not in unique_list:
            unique_list.append((event[1]))
            full_list_of_ticket.append((event[2]))
        else:
            index_of_name=unique_list.index(event[1])
            full_list_of_ticket[index_of_name]+=event[2]
    
    final_list=[]
    for i in range(len(unique_list)):
        final_list.append((unique_list[i], full_list_of_ticket[i]))

            # for item in unique_list:
    final_list.sort()
    return final_list

def analyze_ticket_sales(events):
    # artist_name='Imagine Dragons'
    top_earning_event_id=find_top_earning_event(events)
    imagine_dragons_events=get_events_by_artist(events, 'Imagine Dragons')
    artist_summary=get_artist_sales_summary(events)
    
    return top_earning_event_id, imagine_dragons_events, artist_summary


events = [
    ('EV101', 'The Killers', 5000, 375000),       
    ('EV205', 'Imagine Dragons', 8000, 600000),  
    ('EV102', 'The Killers', 4500, 360000),       
    ('EV301', 'Coldplay', 10000, 950000),        
    ('EV206', 'Imagine Dragons', 8500, 680000)    
]
print(analyze_ticket_sales(events))

# ('EV301', ['EV205', 'EV206'], [('Coldplay', 10000), ('Imagine Dragons', 16500), ('The Killers', 9500)])
events1 = [
    ('EV101', 'Taylor Swift', 12000, 1200000),
    ('EV205', 'Ed Sheeran', 8000, 640000),
    ('EV102', 'Taylor Swift', 15000, 1500000),
    ('EV301', 'Billie Eilish', 6000, 480000),
    ('EV206', 'Ed Sheeran', 9000, 720000),
    ('EV401', 'Adele', 20000, 2500000)
]
print(analyze_ticket_sales(events1))