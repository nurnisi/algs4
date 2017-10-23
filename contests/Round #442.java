    static void c() {
        int n = sc.nextInt();

        if (n == 2) {
            System.out.println(3);
            System.out.println("2 1 2");
            return;
        }

        System.out.println((n - 2) * 2 + 2);

        int mid = n / 2;

        if (n % 2 == 1) mid++;

        int left = mid;
        while (left >= 1) System.out.print(left-- + " ");

        int right = mid + 1;
        while (right <= n) System.out.print(right++ + " ");

        left = 2;
        while (left <= mid) System.out.print(left++ + " ");
        right = n - 1;
        while (right > mid) System.out.print(right-- + " ");
    }

    static void a() {
        String s = sc.nextLine();

        String[] arr = {"Danil", "Olya", "Slava", "Ann", "Nikita"};

        int counter = 0;

        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < arr.length; j++) {
                if (s.charAt(i) == arr[j].charAt(0)) {
                    boolean contains = true;
                    for (int k = 1; k < arr[j].length(); k++) {
                        if (s.charAt(i + k) != arr[j].charAt(k)) {
                            contains = false;
                            break;
                        }
                    }
                    if (contains) counter++;
                }
            }
        }

        if (counter == 1) System.out.println("YES");
        else System.out.println("NO");
    }