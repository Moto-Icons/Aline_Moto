package kalp.motoport.aline;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {
    TextView tgc,bmc,ul;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        Button applyButton = findViewById(R.id.apply_button);
        tgc = findViewById(R.id.TgChannelLink);
        bmc = findViewById(R.id.BuyMeACoffee);
        ul = findViewById(R.id.UpiLink);
        tgc.setMovementMethod(android.text.method.LinkMovementMethod.getInstance());
        bmc.setMovementMethod(android.text.method.LinkMovementMethod.getInstance());
        ul.setMovementMethod(android.text.method.LinkMovementMethod.getInstance());
        applyButton.setOnClickListener(v -> {
            Intent intent = new Intent();
            intent.setClassName("com.motorola.personalize", "com.motorola.personalize.app.IconPacksActivity");
            startActivity(intent);
        });
    }
}