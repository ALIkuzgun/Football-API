import pygame
import csv

pygame.init()

ekran_width = 810
ekran_height = 610
ekran = pygame.display.set_mode((ekran_width, ekran_height))
pygame.display.set_caption("Football Leagues Api")
pygame.display.set_icon(pygame.image.load('icon.png'))

WHITE = (189, 193, 198)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 28)
font3 = pygame.font.SysFont(None, 34)
font2 = pygame.font.Font("font.ttf", 46)

date = "2023"
input_text = ""
input_text2 = ""
lig = ""
league_sel = 0
text_box1 = 0
text_box1_rect = pygame.Rect(110,200,220,34)
text_box2 = 0
text_box2_rect = pygame.Rect(450,200,220,34)
search_rect = pygame.Rect(325,400,120,46)
exit_rect = pygame.Rect(722,556,80,46)
next_rect = pygame.Rect(722,496,80,46)
back_rect = pygame.Rect(10,556,80,46)
search_button = 0
sf = 1

def read_names_from_csv(file_path):
    names = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names.append((row['Number'], row['Team Name'], row['Points'], row['Win'], row['Draw'], row['Lost'], row['Average']))
    return names

def read_names_goals_from_csv(file_path):
    goals = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            goals.append((row['Number'], row['Name'], row['Ps'], row['Age'], row['Team'], row['Goal']))
    return goals

def read_names_assists_from_csv(file_path):
    assists = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            assists.append((row['Numbera'], row['Namea'], row['Psa'], row['Agea'], row['Teama'], row['Assist']))
    return assists

names = read_names_from_csv(f'data/pre_team_data_{date}.csv')
goals = read_names_goals_from_csv(f'data/sp_ga_data_{date}.csv')
assists = read_names_assists_from_csv(f'data/sp_ga_data_{date}.csv')
clock = pygame.time.Clock()

def text_title():
    text = font.render("Team Name", True, (255,255,255))
    text2 = font.render("Points", True, (255,255,255))
    text3 = font.render("W         D         L", True, (255,255,255))
    text4 = font.render("Average", True, (255,255,255))
    ekran.blit(text, (80, 76))
    ekran.blit(text2, (310, 76))
    ekran.blit(text3, (426, 76))
    ekran.blit(text4, (608, 76))

def text_title_ga():
    text = font.render("Name", True, (255,255,255))
    text2 = font.render("Ps", True, (255,255,255))
    text3 = font.render("Age", True, (255,255,255))
    text4 = font.render("Team", True, (255,255,255))
    text5 = font.render("Goal", True, (255,255,255))
    ekran.blit(text, (90, 76))
    ekran.blit(text2, (304, 76))
    ekran.blit(text3, (376, 76))
    ekran.blit(text4, (454, 76))
    ekran.blit(text5, (610, 76))
    text = font.render("Name", True, (255,255,255))
    text2 = font.render("Ps", True, (255,255,255))
    text3 = font.render("Age", True, (255,255,255))
    text4 = font.render("Team", True, (255,255,255))
    text5 = font.render("Assist", True, (255,255,255))
    ekran.blit(text, (90, 336))
    ekran.blit(text2, (304, 336))
    ekran.blit(text3, (376, 336))
    ekran.blit(text4, (454, 336))
    ekran.blit(text5, (606, 336))

running = True
y_offset = 110
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        
        elif event.type == pygame.KEYDOWN:
            if text_box1 == 1:
                if event.key == pygame.K_RETURN:
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                  if len(input_text) < 16:
                    input_text += event.unicode             
            if text_box2 == 1:
                if event.key == pygame.K_RETURN:
                    input_text2 = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text2 = input_text2[:-1]
                else:
                  if len(input_text2) < 4:
                    input_text2 += event.unicode 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if league_sel == 0:
              if text_box1_rect.collidepoint(mouse_pos):
                text_box1 = 1
                text_box2 = 0
              if text_box2_rect.collidepoint(mouse_pos):
                text_box1 = 0
                text_box2 = 1
              if search_rect.collidepoint(mouse_pos):
                search_button = 1
              else:
                search_button = 0
            if league_sel == 1:
              search_button = 0
              if exit_rect.collidepoint(mouse_pos):
                league_sel = 0
                input_text = ""
                input_text2 = ""
                sf = 1
              if sf == 1:
                if next_rect.collidepoint(mouse_pos):
                  sf = 2
              if sf == 2:
                if back_rect.collidepoint(mouse_pos):
                  sf = 1

    ekran.fill((120,120,120))
    if league_sel == 0:
      textx = font2.render(f"Note: 5 major leagues (2020-2023) are valid.", True, BLACK)
      ekran.blit(textx, (80, 500))
      textx = font2.render(f"League:", True, BLACK)
      ekran.blit(textx, (158, 120))
      textx = font2.render(f"Date:", True, BLACK)
      ekran.blit(textx, (515, 120))
      pygame.draw.rect(ekran,(255,255,255),search_rect, border_radius=15)
      textx = font2.render(f"Search", True, BLACK)
      ekran.blit(textx, (334, 392))
      pygame.draw.rect(ekran,(255,255,255),text_box1_rect, border_radius=8)
      pygame.draw.rect(ekran,(255,255,255),text_box2_rect, border_radius=8)
      text_input = font3.render(input_text, True, (20, 0, 0))
      ekran.blit(text_input, (118, 206))
      text_input2 = font3.render(input_text2, True, (20, 0, 0))
      ekran.blit(text_input2, (458, 206))    
      
    if input_text == "Premier League" or input_text == "Premier league" or input_text == "premier league":
      lig = "Pre"
      if input_text2 == "2020":
        date = 2020
        names = read_names_from_csv(f'data/pre_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/pre_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/pre_ga_data_{date}.csv')
      elif input_text2 == "2021":
        date = 2021
        names = read_names_from_csv(f'data/pre_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/pre_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/pre_ga_data_{date}.csv')
      elif input_text2 == "2022":
        date = 2022
        names = read_names_from_csv(f'data/pre_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/pre_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/pre_ga_data_{date}.csv')
      elif input_text2 == "2023":
        date = 2023
        names = read_names_from_csv(f'data/pre_team_data_{date}.csv')    
        goals = read_names_goals_from_csv(f'data/pre_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/pre_ga_data_{date}.csv')  
      else:
         if search_button == 1:
            league_sel = 0
            date = 0
            text = font2.render("Invalid Date!", True, (0,0,0))
            ekran.blit(text, (302, 296))
      if date == 2020 or date == 2021 or date == 2022 or date == 2023:
         if search_button == 1:
            league_sel = 1

    elif input_text == "La Liga" or input_text == "La liga" or input_text == "la liga":
      lig = "Lal"
      if input_text2 == "2020":
        date = 2020
        names = read_names_from_csv(f'data/lal_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/lal_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/lal_ga_data_{date}.csv')
      elif input_text2 == "2021":
        date = 2021
        names = read_names_from_csv(f'data/lal_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/lal_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/lal_ga_data_{date}.csv')
      elif input_text2 == "2022":
        date = 2022
        names = read_names_from_csv(f'data/lal_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/lal_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/lal_ga_data_{date}.csv')
      elif input_text2 == "2023":
        date = 2023
        names = read_names_from_csv(f'data/lal_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/lal_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/lal_ga_data_{date}.csv')
      else:
         if search_button == 1:
            league_sel = 0
            date = 0
            text = font2.render("Invalid Date!", True, (0,0,0))
            ekran.blit(text, (302, 296))
      if date == 2020 or date == 2021 or date == 2022 or date == 2023:
         if search_button == 1:
            league_sel = 1
  
    elif input_text == "Bundesliga" or input_text == "bundesliga":
      lig = "Bl"
      if input_text2 == "2020":
        date = 2020
        names = read_names_from_csv(f'data/bl_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/bl_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/bl_ga_data_{date}.csv')
      elif input_text2 == "2021":
        date = 2021
        names = read_names_from_csv(f'data/bl_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/bl_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/bl_ga_data_{date}.csv')
      elif input_text2 == "2022":
        date = 2022
        names = read_names_from_csv(f'data/bl_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/bl_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/bl_ga_data_{date}.csv')
      elif input_text2 == "2023":
        date = 2023
        names = read_names_from_csv(f'data/bl_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/bl_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/bl_ga_data_{date}.csv')
      else:
         if search_button == 1:
            league_sel = 0
            date = 0
            text = font2.render("Invalid Date!", True, (0,0,0))
            ekran.blit(text, (302, 296))
      if date == 2020 or date == 2021 or date == 2022 or date == 2023:
         if search_button == 1:
            league_sel = 1
  
    elif input_text == "Serie A" or input_text == "serie a" or input_text == "Serie a" or input_text == "serie A":
      lig = "SA"
      if input_text2 == "2020":
        date = 2020
        names = read_names_from_csv(f'data/sa_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/sa_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/sa_ga_data_{date}.csv')
      elif input_text2 == "2021":
        date = 2021
        names = read_names_from_csv(f'data/sa_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/sa_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/sa_ga_data_{date}.csv')
      elif input_text2 == "2022":
        date = 2022
        names = read_names_from_csv(f'data/sa_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/sa_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/sa_ga_data_{date}.csv')
      elif input_text2 == "2023":
        date = 2023
        names = read_names_from_csv(f'data/sa_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/sa_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/sa_ga_data_{date}.csv')
      else:
         if search_button == 1:
            league_sel = 0
            date = 0
            text = font2.render("Invalid Date!", True, (0,0,0))
            ekran.blit(text, (302, 296))
      if date == 2020 or date == 2021 or date == 2022 or date == 2023:
         if search_button == 1:
            league_sel = 1
  
    elif input_text == "Super League" or input_text == "super league" or input_text == "Super league" or input_text == "super League":
      lig = "SL"
      if input_text2 == "2020":
        date = 2020
        names = read_names_from_csv(f'data/sp_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/sp_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/sp_ga_data_{date}.csv')
      elif input_text2 == "2021":
        date = 2021
        names = read_names_from_csv(f'data/sp_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/sp_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/sp_ga_data_{date}.csv')
      elif input_text2 == "2022":
        date = 2022
        names = read_names_from_csv(f'data/sp_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/sp_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/sp_ga_data_{date}.csv')
      elif input_text2 == "2023":
        date = 2023
        names = read_names_from_csv(f'data/sp_team_data_{date}.csv')
        goals = read_names_goals_from_csv(f'data/sp_ga_data_{date}.csv')
        assists = read_names_assists_from_csv(f'data/sp_ga_data_{date}.csv')
      else:
         if search_button == 1:
            league_sel = 0
            date = 0
            text = font2.render("Invalid Date!", True, (0,0,0))
            ekran.blit(text, (302, 296))
      if date == 2020 or date == 2021 or date == 2022 or date == 2023:
         if search_button == 1:
            league_sel = 1
  
    else:
        if search_button == 1:
          lig = ""
          league_sel = 0
          text = font2.render("Invalid League!", True, (0,0,0))
          ekran.blit(text, (282, 296))

    if league_sel == 1:
        pygame.draw.rect(ekran,(255,255,255),exit_rect, border_radius=15)
        textx2 = font2.render(f"Exit", True, BLACK)
        ekran.blit(textx2, (733, 548))
        if sf == 1:
          pygame.draw.rect(ekran,(255,255,255),next_rect, border_radius=15)
          textx2 = font2.render(f"Next", True, BLACK)
          ekran.blit(textx2, (728, 488))
          rect = pygame.Rect(60, 60, 650, 548)
          pygame.draw.rect(ekran, (31,31,31), rect, border_radius=30)  
          for y in range(21): pygame.draw.rect(ekran, (49, 51, 53), (60, y * 24 + 101, 650, 2))
          if lig == "Pre":
            textt = font2.render(f"Premier League {date}", True, BLACK)
            ekran.blit(textt, (220, 0))
          if lig == "Lal":
            textt = font2.render(f"La Liga {date}", True, BLACK)
            ekran.blit(textt, (280, 0))
          if lig == "Bl":
            textt = font2.render(f"Bundesliga {date}", True, BLACK)
            ekran.blit(textt, (250, 0))
          if lig == "SA":
            textt = font2.render(f"Serie A {date}", True, BLACK)
            ekran.blit(textt, (280, 0))
          if lig == "SL":
            textt = font2.render(f"Super League {date}", True, BLACK)
            ekran.blit(textt, (238, 0))
          text_title()
          y_offset = 106  
          for num, name, points, win, draw, lost, average in names:
              text = font.render(f"{num}. {name}", True, WHITE)
              text2 = font.render(f"{points}", True, WHITE)
              text3 = font.render(f"{win}", True, WHITE)
              text4 = font.render(f"{draw}", True, WHITE)
              text5 = font.render(f"{lost}", True, WHITE)
              text6 = font.render(f"{average}", True, WHITE)
              ekran.blit(text, (80, y_offset))
              ekran.blit(text2, (330, y_offset))
              ekran.blit(text3, (424, y_offset))
              ekran.blit(text4, (484, y_offset))
              ekran.blit(text5, (544, y_offset))
              ekran.blit(text6, (634, y_offset))
              y_offset += 24  
        else:
          pygame.draw.rect(ekran,(255,255,255),back_rect, border_radius=15)
          textx2 = font2.render(f"Back", True, BLACK)
          ekran.blit(textx2, (14, 548))
          textx2 = font2.render(f"Top Scorer", True, BLACK)
          ekran.blit(textx2, (314, 1))
          rect = pygame.Rect(70, 60, 650, 180)
          pygame.draw.rect(ekran, (31,31,31), rect, border_radius=30)            
          text_title_ga()
          y_offset2 = 106  
          for number, name, ps, age, team, goal in goals:
              text = font.render(f"{number}. {name}", True, WHITE)
              text2 = font.render(f"{ps}", True, WHITE)
              text3 = font.render(f"{age}", True, WHITE)
              text4 = font.render(f"{team}", True, WHITE)
              text5 = font.render(f"{goal}", True, WHITE)
              ekran.blit(text, (90, y_offset2))
              ekran.blit(text2, (306, y_offset2))
              ekran.blit(text3, (384, y_offset2))
              ekran.blit(text4, (456, y_offset2))
              ekran.blit(text5, (624, y_offset2))
              y_offset2 += 24  
          textx2 = font2.render(f"Assist Leader", True, BLACK)
          ekran.blit(textx2, (314, 260))
          rect = pygame.Rect(70, 320, 650, 180)
          pygame.draw.rect(ekran, (31,31,31), rect, border_radius=30)            
          text_title_ga()
          y_offset2 = 366  
          for numbera, namea, psa, agea, teama, assist in assists:
              text = font.render(f"{numbera}. {namea}", True, WHITE)
              text2 = font.render(f"{psa}", True, WHITE)
              text3 = font.render(f"{agea}", True, WHITE)
              text4 = font.render(f"{teama}", True, WHITE)
              text5 = font.render(f"{assist}", True, WHITE)
              ekran.blit(text, (90, y_offset2))
              ekran.blit(text2, (306, y_offset2))
              ekran.blit(text3, (384, y_offset2))
              ekran.blit(text4, (456, y_offset2))
              ekran.blit(text5, (624, y_offset2))
              y_offset2 += 24  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()