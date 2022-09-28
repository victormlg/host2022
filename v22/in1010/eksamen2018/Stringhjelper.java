class Stringhjelper {

    public static int inneholder(String s, String t) {
        for (int is=0; is <= s.length()-t.length(); is++) {
            boolean eq = true;
            for (int it =0; it<t.length();it++) {
                if (s.charAt(is+it) != t.charAt(it)) {
                    eq = false;
                    break;
                }
            }
            if (eq) return is;
        }
        return -1;
    }
}