from tkinter import *
import copy
import random
from tkinter import messagebox

# --- Constants ---
ROWS = 23
COLS = 23

# Map definition
GAME_MAP = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,2,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,2,0,0,1,0,0,1,0],
    [0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,2,1,0],
    [0,1,1,1,0,1,2,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
    [0,2,0,1,1,1,0,1,1,1,0,0,0,1,1,1,2,1,1,1,1,1,0],
    [0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0],
    [0,1,0,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,2,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,2,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0,1,0],
    [0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0],
    [0,1,1,1,1,1,2,1,1,1,0,0,0,1,1,1,0,1,1,1,0,2,0],
    [0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,2,1,0,1,1,1,0],
    [0,1,2,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,0],
    [0,1,0,0,1,0,0,2,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,2,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

PASSABLE_TILES = {1, 2, 3} # 1: path, 2: sewer (하수구), 3: portal (포탈)

class Player:
    def __init__(self, game_instance, initial_r, initial_c, image_path, entity_type="player"):
        self.game = game_instance
        self.r = initial_r
        self.c = initial_c
        self.entity_type = entity_type
        self.image = PhotoImage(file=image_path)
        self.label = Label(self.game.window, image=self.image, bg="gray")
        self.update_position_on_grid()

    def update_position_on_grid(self):
        self.label.grid(row=self.r, column=self.c, sticky="nesw", padx=2, pady=2)

    def is_valid_move(self, next_r, next_c):
        if not (0 <= next_r < ROWS and 0 <= next_c < COLS):
            return False
        if self.game.game_map[next_r][next_c] not in PASSABLE_TILES:
            return False
        return True

    def move_to(self, next_r, next_c):
        self.r = next_r
        self.c = next_c
        self.update_position_on_grid()

class Thief(Player):
    def __init__(self, game_instance, initial_r, initial_c):
        super().__init__(game_instance, initial_r, initial_c, "./Images./Thief.png", "thief")
        self.keys_collected = 0

    def move(self, dr, dc):
        next_r, next_c = self.r + dr, self.c + dc
        if self.is_valid_move(next_r, next_c):
            self.move_to(next_r, next_c)
            self.game.check_thief_actions() # 열쇠, 문, 포탈 등 도둑의 행동 확인
            self.game.police_move_all() # 도둑 이동 후 경찰 추격

    def check_portal(self):
        # 맵 값 3 (선택된 포탈)에 있을 때만 텔레포트
        if self.game.game_map[self.r][self.c] == 3:
            portal_coords = []
            for r_idx in range(ROWS):
                for c_idx in range(COLS):
                    if self.game.game_map[r_idx][c_idx] == 3:
                        portal_coords.append((r_idx, c_idx))

            # 현재 포탈을 제외한 다른 포탈로 이동
            if (self.r, self.c) in portal_coords:
                portal_coords.remove((self.r, self.c))

            if portal_coords:
                dest_r, dest_c = random.choice(portal_coords)
                self.move_to(dest_r, dest_c)


class Police(Player):
    def __init__(self, game_instance, initial_r, initial_c, police_id):
        super().__init__(game_instance, initial_r, initial_c, "./Images./Police.png", "police")
        self.police_id = police_id
        self.prev_r, self.prev_c = initial_r, initial_c # For blocking previous position

    def move_greedy(self, target_r, target_c, blocked_positions=None, avoid_adjacent_to=None):
        if (self.r, self.c) == (target_r, target_c):
            return (self.r, self.c)

        if blocked_positions is None:
            blocked_positions = set()

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        best_next_step = None
        best_dist2 = float('inf')

        for dr, dc in dirs:
            nr, nc = self.r + dr, self.c + dc

            if not self.is_valid_move(nr, nc):
                continue
            if (nr, nc) in blocked_positions:
                continue

            # ---- 캡처 우선 예외: 후보가 곧바로 도둑 칸이면 바로 선택 ----
            if (nr, nc) == (target_r, target_c):
                return (nr, nc)

            # --- 맨해튼 인접 금지 + 예외(체비쇼프 1 허용) ---
            if avoid_adjacent_to is not None:
                ar, ac = avoid_adjacent_to
                # 현재 후보 칸(nr,nc)이 avoid_adjacent_to와 맨해튼 거리 1이면
                if abs(nr - ar) + abs(nc - ac) == 1:
                    # 하지만 그 후보 칸이 '도둑'과 대각선(체비쇼프 거리 1)이라면 금지 무시하고 허용
                    # 이 예외는 도둑을 잡기 위한 경로를 열어주기 위함
                    if not (max(abs(target_r - nr), abs(target_c - nc)) == 1 and
                            abs(target_r - nr) == 1 and abs(target_c - nc) == 1):
                        continue # 도둑과 대각선도 아니면 여전히 금지

            # 타깃까지의 제곱거리 (유클리드)
            dist2 = (target_r - nr)**2 + (target_c - nc)**2

            if dist2 < best_dist2:
                best_next_step = (nr, nc)
                best_dist2 = dist2

        return best_next_step if best_next_step else (self.r, self.c) # Stay if no valid move


class Game:
    def __init__(self, master):
        self.window = master
        self.window.title("**Equal Grid**")
        self.window.geometry("690x690")
        self.window.resizable(False, False)

        self.game_map = copy.deepcopy(GAME_MAP) # 실제 게임에 사용될 맵
        self.portal_img_sewer = PhotoImage(file="./Images./hole.png") # 하수구 이미지 (MAP 값 2)
        self.portal_img_manhole = PhotoImage(file="./Images./manhole.png") # 포탈 이미지 (MAP 값 3)

        self.randomly_set_portals() # 포탈 랜덤 배치

        self.setup_grid() # 맵 그리기

        # 체크포인트 정보 (초기화)
        self.key_locations = {} # { (r,c) : (Label_obj, key_id) }
        self.door_location = None
        self.key_images = {
            1: PhotoImage(file="./Images./key1.png"),
            2: PhotoImage(file="./Images./key2.png"),
            3: PhotoImage(file="./Images./key3.png")
        }
        self.door_image = PhotoImage(file="./Images./door2.png")

        self.place_checkpoints() # 열쇠와 문 배치

        # 플레이어 및 경찰 객체 생성
        self.thief = Thief(self, 11, 11)
        self.police1 = Police(self, 11, 5, 1)
        self.police2 = Police(self, 11, 16, 2)

        self.bind_keys()

    def randomly_set_portals(self):
        """맵에 있는 원래 2(하수구) 중에서 3개를 골라 3(포탈)으로 변경"""
        sewer_coords = []
        for r_idx in range(ROWS):
            for c_idx in range(COLS):
                if self.game_map[r_idx][c_idx] == 2:
                    sewer_coords.append((r_idx, c_idx))
        
        # 3개의 하수구를 포탈로 선택
        if len(sewer_coords) >= 3:
            selected_portals = random.sample(sewer_coords, 3)
            for r, c in selected_portals:
                self.game_map[r][c] = 3 # 맵 값을 3 (포탈)으로 변경
        else:
            messagebox.showwarning("경고", "맵에 충분한 하수구(2)가 없어 포탈을 3개 설정할 수 없습니다.")


    def setup_grid(self):
        # 그리드 셀 가중치 설정
        for r in range(ROWS):
            self.window.grid_rowconfigure(r, weight=1, uniform="row")
        for c in range(COLS):
            self.window.grid_columnconfigure(c, weight=1, uniform="col")

        # 맵 그리기
        for r in range(ROWS):
            for c in range(COLS):
                tile_type = self.game_map[r][c]
                if tile_type == 1: # 길
                    Label(self.window, bg="gray", relief="solid", borderwidth=1).grid(row=r, column=c, sticky="nesw")
                elif tile_type == 0: # 벽
                    Label(self.window, bg="black").grid(row=r, column=c, sticky="nesw")
                elif tile_type == 2: # 하수구
                    Label(self.window, image=self.portal_img_sewer).grid(row=r, column=c, sticky="nesw")
                elif tile_type == 3: # 포탈
                    Label(self.window, image=self.portal_img_manhole, bg="gray", relief="solid", borderwidth=1).grid(row=r, column=c, sticky="nesw")
                else: # 기타 (혹시 모를 경우)
                    Label(self.window, bg="gray").grid(row=r, column=c, sticky="nesw")


    def place_checkpoints(self):
        # 체크포인트 배치 가능한 4개의 모서리 좌표
        corner_coords = [[1,1], [1,21], [21,1], [21,21]]
        random.shuffle(corner_coords) # 무작위로 섞음

        # 열쇠 3개와 문 1개에 좌표 할당
        key1_pos, key2_pos, key3_pos, door_pos = corner_coords

        # 열쇠 1
        key1_label = Label(self.window, image=self.key_images[1], bg="gray")
        key1_label.grid(row=key1_pos[0], column=key1_pos[1], sticky="nesw", padx=3, pady=3)
        self.key_locations[tuple(key1_pos)] = (key1_label, 1)

        # 열쇠 2
        key2_label = Label(self.window, image=self.key_images[2], bg="gray")
        key2_label.grid(row=key2_pos[0], column=key2_pos[1], sticky="nesw", padx=3, pady=3)
        self.key_locations[tuple(key2_pos)] = (key2_label, 2)

        # 열쇠 3
        key3_label = Label(self.window, image=self.key_images[3], bg="gray")
        key3_label.grid(row=key3_pos[0], column=key3_pos[1], sticky="nesw", padx=3, pady=3)
        self.key_locations[tuple(key3_pos)] = (key3_label, 3)

        # 문
        self.door_label = Label(self.window, image=self.door_image, bg="white")
        self.door_label.grid(row=door_pos[0], column=door_pos[1], sticky="nesw", padx=2, pady=2)
        self.door_location = tuple(door_pos)


    def check_thief_actions(self):
        thief_pos = (self.thief.r, self.thief.c)

        # 1. 열쇠 획득 확인
        if thief_pos in self.key_locations:
            key_label, key_id = self.key_locations[thief_pos]
            key_label.destroy() # 열쇠 객체 제거
            del self.key_locations[thief_pos] # 딕셔너리에서 제거
            self.thief.keys_collected += 1
            print(f"Key {key_id} collected! Total keys: {self.thief.keys_collected}")

        # 2. 문 확인
        if thief_pos == self.door_location:
            if self.thief.keys_collected >= 3:
                messagebox.showinfo("탈출 성공!", "축하드립니다! 게임을 종료합니다.")
                self.window.destroy()
            else:
                messagebox.showinfo("탈출 실패", f"열쇠가 {3 - self.thief.keys_collected}개 부족합니다!")
        
        # 3. 포탈 확인 (하수구는 맵 값 2, 포탈은 맵 값 3)
        self.thief.check_portal()


    def police_move_all(self):
        thief_pos = (self.thief.r, self.thief.c)

        # 1. Store police1's current position as its 'previous' for police2's blocking
        self.police1.prev_r, self.police1.prev_c = self.police1.r, self.police1.c

        # 2. Calculate police1's next move, avoiding police2's current position
        next_r1, next_c1 = self.police1.move_greedy(
            thief_pos[0], thief_pos[1],
            avoid_adjacent_to=(self.police2.r, self.police2.c)
        )

        # 3. Define blocked positions for police2:
        #    - Police1's *new* position (next_r1, next_c1)
        #    - Police1's *previous* position (police1.prev_r, police1.prev_c)
        #    - Exclude thief's position from blocked_for_p2, to allow capture
        blocked_for_p2 = {(next_r1, next_c1), (self.police1.prev_r, self.police1.prev_c)}
        if thief_pos in blocked_for_p2:
            blocked_for_p2.remove(thief_pos)

        # 4. Calculate police2's next move, avoiding police1's new position and other blocked spots
        next_r2, next_c2 = self.police2.move_greedy(
            thief_pos[0], thief_pos[1],
            blocked_positions=blocked_for_p2,
            avoid_adjacent_to=(next_r1, next_c1)
        )

        # To prevent police2 moving to police1's exact spot if it's not the thief's position
        if (next_r2, next_c2) == (next_r1, next_c1) and (next_r2, next_c2) != thief_pos:
            next_r2, next_c2 = self.police2.r, self.police2.c # Police2 stays put

        # 5. Apply the moves
        self.police1.move_to(next_r1, next_c1)
        self.police2.move_to(next_r2, next_c2)

        self.check_game_over()

    def check_game_over(self):
        if (self.police1.r, self.police1.c) == (self.thief.r, self.thief.c) or \
           (self.police2.r, self.police2.c) == (self.thief.r, self.thief.c):
            messagebox.showinfo("게임 종료", "잡힘! 게임이 종료됩니다.")
            self.window.destroy()

    def bind_keys(self):
        self.window.bind("<Up>", lambda event: self.thief.move(-1, 0))
        self.window.bind("<Left>", lambda event: self.thief.move(0, -1))
        self.window.bind("<Down>", lambda event: self.thief.move(1, 0))
        self.window.bind("<Right>", lambda event: self.thief.move(0, 1))


if __name__ == "__main__":
    root = Tk()
    game = Game(root)
    root.mainloop()