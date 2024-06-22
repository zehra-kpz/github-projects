# To-Do List Uygulaması

def display_menu():
    print("\nTo-Do List Uygulaması")
    print("1. Görevleri Görüntüle")
    print("2. Görev Ekle")
    print("3. Görev Sil")
    print("4. Görev Düzenle")
    print("5. Görevi Tamamla")
    print("6. Kategorilere Göre Görevleri Görüntüle")
    print("7. Çıkış")

def display_tasks(tasks):
    if not tasks:
        print("Hiç görev yok.")
    else:
        print("\nGörevler:")
        for idx, task in enumerate(tasks, start=1):
            status = "Tamamlandı" if task["completed"] else "Tamamlanmadı"
            print(f"{idx}. {task['name']} [{task['category']}] [{status}]")

def display_tasks_by_category(tasks):
    if not tasks:
        print("Hiç görev yok.")
    else:
        categories = set(task['category'] for task in tasks)
        for category in categories:
            print(f"\nKategori: {category}")
            for idx, task in enumerate(tasks, start=1):
                if task['category'] == category:
                    status = "Tamamlandı" if task["completed"] else "Tamamlanmadı"
                    print(f"{idx}. {task['name']} [{status}]")

def add_task(tasks):
    task_name = input("Yeni görev girin: ")
    task_category = input("Görev kategorisini girin: ")
    #Kategoriler başlangıçta tablo olarak verilebilir
    tasks.append({"name": task_name, "category": task_category, "completed": False})
    print(f"Görev eklendi: {task_name}")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Silmek istediğiniz görevin numarasını girin: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Görev silindi: {removed_task['name']}")
        else:
            print("Geçersiz görev numarası.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def edit_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Düzenlemek istediğiniz görevin numarasını girin: "))
        if 1 <= task_num <= len(tasks):
            new_name = input("Yeni görev adını girin: ")
            new_category = input("Yeni görev kategorisini girin: ")
            tasks[task_num - 1]["name"] = new_name
            tasks[task_num - 1]["category"] = new_category
            print(f"Görev güncellendi: {new_name}")
        else:
            print("Geçersiz görev numarası.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def complete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Tamamlamak istediğiniz görevin numarasını girin: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Görev tamamlandı: {tasks[task_num - 1]['name']}")
        else:
            print("Geçersiz görev numarası.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Seçiminizi yapın: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            complete_task(tasks)
        elif choice == '6':
            display_tasks_by_category(tasks)
        elif choice == '7':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")
    input("Programdan çıkmak için Enter'a basın...")

if __name__ == "__main__":
    main()
