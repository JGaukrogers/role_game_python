package cat.judith.stopsmoking;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class SeeStatistics extends AppCompatActivity {

    private TextView cigsSmokedView;
    private TextView moneySmokedView;

    //TODO: get from settings
    private double price = 5;
    private int cigsPerPacket = 20;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_see_statistics);

        cigsSmokedView = (TextView) findViewById(R.id.cigsSmokedView);
        moneySmokedView = (TextView) findViewById(R.id.monexSmokedView);

        int totalCigsSmoked = getTotalCigarettesSmoked();
        cigsSmokedView.setText(totalCigsSmoked + " cigarettes smoked");
        moneySmokedView.setText(getTotalMoneySmoked(totalCigsSmoked) + " € smoked");

    }

    private int getTotalCigarettesSmoked() {

        int sum_cigs_smoked;

        CigarettesSmokedDB dbHelper = new CigarettesSmokedDB(this.getApplicationContext());
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        Cursor c = db.rawQuery(CigarettesSmokedDB.SQL_GET_SUM, null);
        if(c.moveToFirst())
            sum_cigs_smoked = c.getInt(0);
        else
            sum_cigs_smoked = -1;
        db.close();

        return sum_cigs_smoked;
    }

    private double getTotalMoneySmoked(int totalCigarettes) {
        double totalMoney = getPriceForSingleCig() * totalCigarettes;
        return totalMoney;
    }

    private double getPriceForSingleCig() {
        return price / cigsPerPacket;
    }

}
