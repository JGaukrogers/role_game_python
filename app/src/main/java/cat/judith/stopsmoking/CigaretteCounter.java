package cat.judith.stopsmoking;

import android.content.ContentValues;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.TextView;

import java.util.Calendar;
import java.util.Locale;

public class CigaretteCounter extends AppCompatActivity {

    private TextView numCigsView;
    private int todaysDate;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cigarette_counter);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        numCigsView = (TextView) findViewById(R.id.numCigsText);

//        CigarettesSmokedDB dbHelper = new CigarettesSmokedDB(this.getApplicationContext());
//        CigarettesSmokedDB.init(this.getApplicationContext());

        // Look if DB has entry for today
        CigarettesSmokedDB dbHelper = new CigarettesSmokedDB(this.getApplicationContext());
        SQLiteDatabase db = dbHelper.getReadableDatabase();
        String[] projection = {
                CigarettesSmokedDB.COLUMN_NAME_ENTRY_ID,
                CigarettesSmokedDB.COLUMN_NAME_SMOKED
        };
        String selection = CigarettesSmokedDB.COLUMN_NAME_ENTRY_ID + " = ?";
        Calendar cAux = Calendar.getInstance(Locale.getDefault());
        todaysDate = cAux.get(Calendar.YEAR) * 10000
                + (cAux.get(Calendar.MONTH) + 1) * 100
                + cAux.get(Calendar.DAY_OF_MONTH);
        String[] selectionArgs = {
                String.valueOf(todaysDate)
        };
        Cursor c = db.query(
                CigarettesSmokedDB.TABLE_NAME,  // The table to query
                projection,                     // The columns to return
                selection,                      // The columns for the WHERE clause
                selectionArgs,                  // The values for the WHERE clause
                null,                           // don't group the rows
                null,                           // don't filter by row groups
                null                            // don't sort
        );
        int count = c.getCount();
        if( count == 0){
            // Add entry and show to user
            numCigsView.setText("0");
            insertToDatabase(0, dbHelper);
        }
        else{
            //Get entry and show to user
            c.moveToFirst();
            String itemId = c.getString(c.getColumnIndex(CigarettesSmokedDB.COLUMN_NAME_SMOKED));
            numCigsView.setText(itemId);
        }
        c.close();
    }

    /*
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_cigarette_counter, menu);
        return true;
    }
    */

    /*
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
    */

    private void insertToDatabase(int smoked, CigarettesSmokedDB dbHelper) {
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        // Create a new map of values, where column names are the keys
        ContentValues values = new ContentValues();
        values.put(CigarettesSmokedDB.COLUMN_NAME_ENTRY_ID, todaysDate);
        values.put(CigarettesSmokedDB.COLUMN_NAME_SMOKED, smoked);

        // Insert the new row, returning the primary key value of the new row
        db.insert(
                CigarettesSmokedDB.TABLE_NAME,
                null,
                values);
    }

    private void updateToDatabase(int smoked, CigarettesSmokedDB dbHelper) {
        SQLiteDatabase db = dbHelper.getWritableDatabase();

        // Create a new map of values, where column names are the keys
        ContentValues values = new ContentValues();
        values.put(CigarettesSmokedDB.COLUMN_NAME_SMOKED, smoked);
        String[] where = {String.valueOf(todaysDate)};

        // Insert the new row, returning the primary key value of the new row
        db.update(
                CigarettesSmokedDB.TABLE_NAME,
                values,
                CigarettesSmokedDB.COLUMN_NAME_ENTRY_ID + "=?",
                where);
    }

    public void addOneCig(View view) {
        String aux = String.valueOf(numCigsView.getText());
        Integer numCigs = Integer.decode(aux) + 1;
        numCigsView.setText(String.valueOf(numCigs));

        CigarettesSmokedDB dbHelper = new CigarettesSmokedDB(this.getApplicationContext());
        updateToDatabase(numCigs, dbHelper);
    }

    public void seeStatistics(View view) {
        Intent intent = new Intent(this, SeeStatistics.class);
        startActivity(intent);
    }

    public void settings(View view){
        Intent intent = new Intent(this, Settings.class);
        startActivity(intent);
    }
}
